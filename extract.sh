rm testingimages/*.jpg
rm Objects/*.jpg
rm poses/*.jpg

python names.py

cd darknet && ./darknet detector test cfg/coco.data cfg/yolov3-spp.cfg yolov3-spp.weights -thresh 0.05 -ext_output -dont_show -out result.json < data/train.txt
cd ..

cp ../Video1/video-to-test/*.jpg ./testingimages/


python extract.py 



