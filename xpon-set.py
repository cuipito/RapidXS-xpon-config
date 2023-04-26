import sys
import string
import hashlib
import paramiko

if len(sys.argv) < 7:
    print("Please provide the following arguments: host, username, password, macAddress, PONvendor, GPON_SN")
    sys.exit(1)

host = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
mac_address = sys.argv[4].strip().replace(':','')
pon_vendor = sys.argv[5]
gpon_sn = sys.argv[6]



# Remove ":" characters from the converted ASCII string
#mac_address_ascii = mac_address_ascii.replace(":", "")

# Check if PONvendor argument contains only alphabetic characters
if not pon_vendor.isalpha():
    print("Error: PONvendor argument should only contain alphabetic characters.")
    sys.exit(1)


if len(mac_address) != 12:
	sys.exit("Mac address must be 12 hex digits (6 bytes)")

if not all(c in string.hexdigits for c in mac_address):
	sys.exit("Mac address can only contain 0-9, A-F characters (hex digits)")


cmacPrefix = 'hsgq1.9a'
hashText = cmacPrefix+mac_address.upper()
encodedText = hashText.encode('ascii')
md5Hash = hashlib.md5(encodedText).digest().hex()

# Combine PONvendor and GPON_SN arguments
gpon_sn_combined = pon_vendor + gpon_sn

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, username=username, password=password)
    print("SSH connection established.")

    # Check if the SSH connection is active
    if ssh.get_transport() is None or not ssh.get_transport().is_active():
        print("SSH connection is not active.")
        sys.exit(1)
    # Execute first command on the SSH server
    setmac = 'flash set ELAN_MAC_ADDR {}'.format(mac_address.lower())
    stdin, stdout, stderr = ssh.exec_command(setmac)

    # Print setmac output
    print("Setting ELAN_MAC_ADDR:", setmac)
    #print("Output:")
    for line in stdout:
        print(line.strip())

    # Execute second command on the SSH server
    setmackey = 'flash set MAC_KEY {}'.format(md5Hash.lower())
    stdin, stdout, stderr = ssh.exec_command(setmackey)

    # Print command2 output
    print("Setting MAC_KEY:", setmackey)
    #print("Output:")
    for line in stdout:
        print(line.strip())

    # Execute third command on the SSH server
    setsn = 'flash set GPON_SN {}'.format(gpon_sn_combined)
    stdin, stdout, stderr = ssh.exec_command(setsn)

    # Print command3 output
    print("Setting combined GPON vendor name and GPON Serial:", setsn)
    #print("Output:")
    for line in stdout:
        print(line.strip())

    # Execute forth command on the SSH server
    setvendor = 'flash set PON_VENDOR_ID {}'.format(pon_vendor)
    stdin, stdout, stderr = ssh.exec_command(setvendor)

    # Print setvendor output
    print("Setting PON_VENDOR_ID:", setvendor)
   # print("Output:")
    for line in stdout:
        print(line.strip())


    ssh.close()
    print("SSH connection closed.")

except paramiko.AuthenticationException:
    print("Authentication failed. Please check your credentials.")
except paramiko.SSHException as ssh_exception:
    print("Error occurred while establishing SSH connection:", str(ssh_exception))
except Exception as e:
    print("Error:", str(e))
del ssh, stdin, stdout, stderr

