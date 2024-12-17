# Contributing to Adobe CCF Policy Generator

First off, thank you for considering contributing to Adobe CCF Policy Generator! It's people like you that make this tool better for everyone.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct. Please report unacceptable behavior to [project maintainers].

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues list as you might find that you don't need to create one. When you create a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples** to demonstrate the steps
* **Describe the behavior you observed**
* **Explain the behavior you expected**
* **Include screenshots or logs** if possible

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a detailed description of the suggested enhancement**
* **Explain why this enhancement would be useful**
* **List some examples of how it would be used**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code follows the existing style
6. Issue the pull request!

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/markac007/adobe-ccf-policy-generator.git
cd adobe-ccf-policy-generator
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Run tests:
```bash
python -m pytest
```

## Style Guidelines

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Python Style Guide

* Follow PEP 8
* Use meaningful variable names
* Include docstrings for functions and classes
* Add comments for complex logic

### Documentation Style Guide

* Use Markdown for documentation
* Include code examples when relevant
* Keep language clear and concise
* Update README.md if needed

## Project Structure

When contributing, please maintain the existing project structure:

```
backend/
├── src/                     # Source code
├── scripts/                 # Scripts and entry points
├── templates/               # Template files
├── data/                    # Data files
│   ├── processed/          # Processed JSON data
│   └── raw/                # Raw CSV data
└── tests/                  # Test files
```

## Testing

* Write tests for new features
* Update tests when modifying existing features
* Ensure all tests pass before submitting PR
* Include both unit tests and integration tests when applicable

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_specific.py

# Run with coverage
python -m pytest --cov=src
```

## Additional Notes

### Issue and Pull Request Labels

* `bug` - Confirmed bugs or reports likely to be bugs
* `enhancement` - New feature or request
* `documentation` - Documentation only changes
* `help-wanted` - Extra attention is needed
* `good-first-issue` - Good for newcomers

## Recognition

Contributors will be recognized in the following ways:
* Listed in CONTRIBUTORS.md
* Mentioned in release notes for significant contributions
* Added to GitHub contributors list

## Questions?

Don't hesitate to ask questions about contributing. You can:
* Open an issue with your question
* Contact the maintainers directly
* Join our community discussions

Thank you for contributing to Adobe CCF Policy Generator! 