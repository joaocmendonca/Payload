IP=$1
HOSTNAME=$2
FILE="/etc/hosts"

{
  echo -e "${IP}\t${HOSTNAME}" >> ${FILE}
} || {
  echo "Target Server does not have ownership of file ${FILE}"
}
