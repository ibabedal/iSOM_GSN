# A ready use environment to use to apply iSOM_GSN algorithm.

The original link mentioned here: https://github.com/NaziaFatima/iSOM_GSN

if you want to test the code of tensorflow 1.x , please use the docker file in linux_version_v1 and please run the below commands (ensure you are in the same directory):

`
docker build -t isom_gsn:v1 -f ./Dockerfile .
`

`
docker run -it isom_gsn:v1
`

if you want to test the code of tensorflow 2.x , please use the docker file in linux_version_v2 and please run the below commands (ensure you are in the same directory):

`
docker build -t isom_gsn:v2 -f ./Dockerfile .
`

`
docker run -it isom_gsn:v2
`