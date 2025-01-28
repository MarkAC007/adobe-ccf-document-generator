import pandas as pd
import json
import logging
from pathlib import Path
import numpy as np

class DataProcessor:
    def __init__(self, raw_data_path, processed_data_path):
        """Initialize with paths as strings"""
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path
        print(f"\n=== DataProcessor Initialization ===")
        print(f"Raw data path: {self.raw_data_path}")
        print(f"Processed data path: {self.processed_data_path}")
        self.setup_logging()

    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def clean_framework_references(self, value):
        """
        Clean framework references by handling multiple formats:
        - Newline-separated strings
        - Comma-separated strings
        - Single values
        - Arrays/lists
        """
        # Handle arrays/lists
        if isinstance(value, (list, np.ndarray)):
            return [str(v).strip().replace('¿½', '') for v in value if str(v).strip()]
        
        # Handle NaN/None
        if isinstance(value, float) and pd.isna(value):
            return []
        
        if value is None:
            return []
            
        # Convert value to string to handle any numeric values
        value_str = str(value).replace('¿½', '')
        
        # First split by newlines if present
        items = value_str.split('\n')
        
        # Process each item for comma separation
        cleaned_refs = []
        for item in items:
            # Split by comma and clean each reference
            refs = [ref.strip() for ref in item.split(',') if ref.strip()]
            cleaned_refs.extend(refs)
            
        return cleaned_refs

    def clean_text_field(self, value: str) -> str:
        """
        Clean text fields by removing special characters and extra whitespace.
        
        Args:
            value (str): Raw text value
            
        Returns:
            str: Cleaned text value
        """
        if pd.isna(value):
            return ""
        
        # Convert to string and clean
        text = str(value)
        # Replace smart quotes and other special chars
        text = text.replace('\u2018', "'").replace('\u2019', "'")
        text = text.replace('\u201c', '"').replace('\u201d', '"')
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text

    def clean_audit_artifacts(self, value: str) -> list[str]:
        """
        Clean audit artifacts string into a list of distinct artifact IDs.
        
        Args:
            value (str): Raw audit artifacts string
            
        Returns:
            list[str]: List of cleaned artifact IDs
        """
        if pd.isna(value):
            return []
            
        # Split on newlines and clean each artifact ID
        artifacts = [
            artifact.strip() 
            for artifact in str(value).split('\n')
            if artifact.strip()
        ]
        
        # Remove duplicates while preserving order
        return list(dict.fromkeys(artifacts))

    def create_controls_mapping(self, controls_df: pd.DataFrame) -> dict:
        """
        Create a mapping of controls to framework references.
        
        Args:
            controls_df: DataFrame containing control framework mappings
            
        Returns:
            dict: Mapping of control IDs to their framework references
        """
        framework_columns = [
            'nist_cybersecurity_ref', 'bsi_c5_ref', 'cis_v8_ref', 'mlps_ref', 
            'iso_22301_ref', 'cyber_essentials_uk_ref', 'ens_ref', 'iso_27001_ref', 
            'iso_27002_ref', 'iso_27017_ref', 'iso_27018_ref', 'tx_ramp_L1_ref',
            'fedramp_tailored_ref', 'fedramp_moderate_ref', 'hipaa_security_ref',
            'irap_ref', 'ismap_ref', 'mas_ref', 'pci_dss_v4_ref', 'kfsi_ref', 'soc_2_ref'
        ]
        
        mapping = {}
        for _, row in controls_df.iterrows():
            control_id = row['ccf_id']
            framework_map = {}
            
            for framework in framework_columns:
                value = row.get(framework)
                # Clean and keep the actual reference value
                framework_map[framework] = self.clean_framework_references(value)
                    
            mapping[control_id] = framework_map
            
        return mapping

    def create_erl_mapping(self, erl_df: pd.DataFrame) -> dict:
        """
        Create a mapping of evidence references.
        
        Args:
            erl_df: DataFrame containing evidence reference library
            
        Returns:
            dict: Mapping of evidence references with their details
        """
        erl_mapping = {}
        
        for _, row in erl_df.iterrows():
            reference_id = row['reference_id']
            erl_mapping[reference_id] = {
                'evidence_domain': row['evidence_domain'],
                'evidence_title': row['evidence_title']
            }
            
        return erl_mapping

    def convert_csv_to_json(self):
        """
        Convert CSV files to JSON format with improved data cleaning and validation.
        
        Raises:
            FileNotFoundError: If source CSV files are not found
            ValueError: If required columns are missing
        """
        try:
            print(f"Processing CSV files from {self.raw_data_path} to {self.processed_data_path}")
            
            # Read CSVs with explicit encoding
            controls_df = pd.read_csv(
                self.raw_data_path / 'controls_v2.csv',
                encoding='utf-8',
                na_values=['', 'NA', 'N/A']
            )
            guidance_df = pd.read_csv(
                self.raw_data_path / 'control_guidance.csv', 
                encoding='utf-8',
                na_values=['', 'NA', 'N/A']
            )
            erl_df = pd.read_csv(
                self.raw_data_path / 'erl.csv',
                encoding='utf-8',
                na_values=['', 'NA', 'N/A']
            )
            
            # Validate required columns
            required_columns = {
                'ccf_id', 'control_domain', 'control_name',
                'control_description', 'policy_standard'
            }
            if not required_columns.issubset(guidance_df.columns):
                missing = required_columns - set(guidance_df.columns)
                raise ValueError(f"Missing required columns: {missing}")

            # Clean text fields
            text_columns = [
                'control_description', 'implementation_guidance',
                'testing_procedure', 'control_name'
            ]
            for col in text_columns:
                if col in guidance_df.columns:
                    guidance_df[col] = guidance_df[col].apply(self.clean_text_field)

            # Convert audit artifacts to arrays before JSON conversion
            guidance_df['audit_artifacts'] = guidance_df['audit_artifacts'].apply(
                self.clean_audit_artifacts
            )

            # Process framework columns in controls_df
            framework_columns = [
                'nist_cybersecurity', 'bsi_c5', 'cis_v8', 'mlps', 'iso_22301',
                'cyber_essentials_uk', 'ens', 'iso_27001', 'iso_27002', 'iso_27017',
                'iso_27018', 'tx_ramp_L1', 'fedramp_tailored', 'fedramp_moderate',
                'hipaa_security', 'irap', 'ismap', 'mas', 'pci_dss_v4', 'kfsi', 'soc_2'
            ]
            
            # Clean framework references and standardize values
            for column in controls_df.columns:
                if column.endswith('_ref'):
                    controls_df[column] = controls_df[column].apply(self.clean_framework_references)
                elif column in framework_columns:
                    controls_df[column] = controls_df[column].apply(
                        lambda x: 'X' if pd.notnull(x) and str(x).strip().upper() == 'X' else None
                    )

            # Convert to dictionaries while ensuring audit_artifacts remains as array
            controls_records = controls_df.to_dict(orient='records')
            guidance_records = guidance_df.to_dict(orient='records')
            
            # Create final JSON structures
            controls_json = {"controls": controls_records}
            guidance_json = {"controls": guidance_records}
                
            # Save all files
            files_to_save = [
                ('controls_v2.json', controls_json),
                ('control_guidance.json', guidance_json),
                ('controls_mapping.json', self.create_controls_mapping(controls_df)),
                ('erl.json', self.create_erl_mapping(erl_df))
            ]
            
            for filename, data in files_to_save:
                file_path = self.processed_data_path / filename
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Created: {file_path}")
                
            print("\nSuccessfully converted CSV files to JSON format")
                
        except FileNotFoundError as e:
            logging.error(f"Source CSV file not found: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error processing CSV files: {str(e)}")
            raise

    def get_processed_controls(self):
        """Load and return processed controls data"""
        try:
            print(f"Loading controls from: {self.raw_data_path}")
            with open(self.raw_data_path, 'r', encoding='utf-8') as f:
                controls_data = json.load(f)
            print(f"Successfully loaded {len(controls_data.get('controls', []))} controls")
            return controls_data
        except Exception as e:
            print(f"Error loading controls: {str(e)}")
            raise

    def get_controls_by_policy(self, policy_name: str) -> list:
        """Retrieve controls for specified policy"""
        logging.debug(f"Retrieving controls for policy: {policy_name}")
        
        guidance_path = self.processed_data_path / 'control_guidance.json'
        if not guidance_path.exists():
            raise FileNotFoundError("Control guidance JSON not found. Run convert_csv_to_json first.")
            
        with open(guidance_path) as f:
            data = json.load(f)
        
        controls = [c for c in data["controls"] 
                   if c["policy_standard"] == policy_name]
        
        logging.debug(f"Found {len(controls)} controls: {[c['ccf_id'] for c in controls]}")
        return controls

    def get_framework_mappings(self, control_ids: list, frameworks: list) -> dict:
        """Get framework mappings for specified controls and frameworks"""
        logging.debug(f"Getting framework mappings for controls: {control_ids}")
        
        controls = self.get_processed_controls()
        
        mappings = {}
        for control in controls["controls"]:
            if control["ccf_id"] in control_ids:
                control_mappings = {}
                for framework in frameworks:
                    ref_key = f"{framework.lower()}_ref"
                    if ref_key in control:
                        control_mappings[framework] = control[ref_key]
                mappings[control["ccf_id"]] = control_mappings
                
        return mappings
