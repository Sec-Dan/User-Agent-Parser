
# User-Agent Parser

## Overview

The User-Agent Parser is a web application built with Python and Flask that parses incoming HTTP request headers to identify and extract information about the user agent. It is deployed on Heroku and serves the purpose of detecting various details about the client's browser, operating system, and device.

## Features

- **Parse User-Agent Strings**: Extract and display detailed information from User-Agent headers.
- **Responsive UI**: Simple and intuitive web interface to input and analyze User-Agent strings.
- **Deployment on Heroku**: Easily scalable and accessible via a public URL.

## Technology Stack

- **Backend**: Python, Flask
- **Web Server**: Gunicorn
- **Hosting**: Heroku
- **Dependencies**:
  - `flask`
  - `user_agents`

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository:

   \`\`\`bash
   git clone https://github.com/yourusername/user-agent-parser.git
   cd user-agent-parser
   \`\`\`

2. Install dependencies:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

### Running Locally

1. Set environment variables (optional):

   \`\`\`bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   \`\`\`

2. Start the Flask development server:

   \`\`\`bash
   flask run
   \`\`\`

3. Access the application at \`http://127.0.0.1:5000/\`.

## Usage

1. Visit https://agent.dansec.red.
2. Input a User-Agent string in the text box and click "Submit".
3. The application will display parsed details, including the browser, operating system, and device information.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
