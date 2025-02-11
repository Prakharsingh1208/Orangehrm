# Selenium Automation Framework
Selenium Automation Framework<br>
This project is a Selenium-based automation framework built from scratch using Python and pytest. It is designed for automated testing of web applications, with advanced utilities such as logging, screenshot capturing, multi-test execution, and configuration file management. The framework uses Selenium 4.x and pytest for test orchestration and reporting.<br>
<br>
Project Structure<br>
bash<br>
Copy<br>
Edit<br>
.<br>
├── .idea/                      # Project configuration (IDE-specific files)
├── .pytest_cache/              # pytest cache files
├── .venv/                      # Virtual environment containing dependencies
├── tests/                      # Test scripts for different functionalities
├── utils/                      # Utility functions for logging, screenshots, etc.
├── config/                     # Configuration files (e.g., test environment)
├── reports/                    # Test reports and logs
└── README.md                   # Project documentation (this file)
Features
Selenium 4.x: For web automation.
pytest Integration: For test execution, assertions, and reporting.
Screenshot Capturing: Captures screenshots on test failure.
Logging Support: Logs all critical actions and test results.
Configuration Management: Supports multiple test environments using configuration files.
Multi-Test Execution: Run multiple test cases in parallel.
