RapidXS-Gpon-conf-gen
Description

RapidXS-Gpon-conf-gen is a Python script that sets up the necessary configuration parameters required for the ISP provider called RapidXS. It automates the process of configuring a device over an SSH connection, handling tasks like setting MAC addresses, generating hashes, and configuring vendor-specific settings.
Installation Requirements

This script requires paramiko for SSH communication with remote devices. It is compatible with all versions of Python.
Install paramiko:

bash

pip install paramiko

Setup Instructions

To run this script, you can use any of the following methods:

    Using Python directly:
        Download the script and navigate to the directory containing the script.
        Ensure paramiko is installed.
        Run the script using Python:

        bash

    python rapidxs_gpon_conf_gen.py <host> <username> <password> <macAddress> <PONvendor> <GPON_SN>

Using a Virtual Environment:

    Create a virtual environment (optional but recommended):

    bash

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install paramiko:

bash

pip install paramiko

Run the script:

bash

        python rapidxs_gpon_conf_gen.py <host> <username> <password> <macAddress> <PONvendor> <GPON_SN>

Usage

Run the script from the command line, providing the required arguments:

bash

python rapidxs_gpon_conf_gen.py <host> <username> <password> <macAddress> <PONvendor> <GPON_SN>

Example:

bash

python rapidxs_gpon_conf_gen.py 192.168.1.1 admin admin123 00:1A:2B:3C:4D:5E HUAWEI GPON12345678

Configuration

The script requires the following parameters:

    host: The IP address or hostname of the device you want to configure.
    username: The SSH username to access the device.
    password: The SSH password for the specified username.
    macAddress: The MAC address of the device, provided as a string (e.g., 00:1A:2B:3C:4D:5E).
    PONvendor: The vendor name associated with the PON device (should only contain alphabetic characters).
    GPON_SN: The GPON serial number of the device, which will be combined with the vendor name during configuration.

Error Handling

Below are some common errors that may occur when running this script:

    Invalid MAC Address:
        Occurs if the provided MAC address is not 12 hexadecimal characters.
        Example message: Mac address must be 12 hex digits (6 bytes).

    Non-Alphabetic PON Vendor:
        Occurs if the PON vendor contains non-alphabetic characters.
        Example message: Error: PONvendor argument should only contain alphabetic characters.

    SSH Connection Issues:
        Possible reasons include incorrect credentials or network issues.
        Example messages:
            Authentication failed. Please check your credentials.
            Error occurred while establishing SSH connection: <error details>

    Connection Timeout:
        Occurs if the SSH connection cannot be established within a certain time.

Contributing

Contributions are welcome! If you'd like to improve this script or fix any issues, please follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature/YourFeature).
    Make your changes.
    Commit your changes (git commit -m 'Add some feature').
    Push to the branch (git push origin feature/YourFeature).
    Open a pull request.

License

This project is licensed under the MIT License - you are free to use, modify, and distribute this software for personal or commercial use.
