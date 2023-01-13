#!/bin/bash

# Get the file name and stack name
cloudformation_file=$1

# aws download the hash.txt from s3 bucket
aws s3 cp s3://oldmengrinding-cicd/hash.txt hash.txt


# hash_file="$(<hash.txt)"
# value="$(<$hash_file)"


# # Get the hashes of the files
# hash1=$(md5sum $file | awk '{print $1}')
# hash2=$(echo $value | awk '{print $1;}')


# # Compare the hashes
# if [ "$hash1" != "$hash2" ]; then
#     echo "The files are different, updating the stack..."
#     aws cloudformation update-stack --stack-name $stack_name --template-body file://$file

    # upload the updated hash into a txt in oldmengrinding bucket
    # update the stack
# else
#     echo "The files are identical, no update needed."
# fi