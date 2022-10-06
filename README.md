# Is It Impressionism

Art/digital classification by meta features. Dictinctive features that difire a painting from a usual digital picture are style, narrative and others. 
The goals are:
1) create a Flask API server by deploying PyTorch (CNN) model 
2) Investigate 2 problems: 
- What meta features can be useful? 
- Explore various CNN architectures as an aproach to a classification paradigm. 

Don't consider pairs of images: the painting and the photograph of this painting. 

### Demo 
ResNet18 was used for the demo.   
The balanced Train set is 1246 includes impressionism paintings and various digital images.   
The yoy test set is 10, the test accuracy of 81%.     

![Screenshot from 2022-10-06 14-53-01](https://user-images.githubusercontent.com/14224692/194429610-eae1cc6c-b5c4-4d9c-b8a1-8e1a1000d483.png)

![Screenshot from 2022-10-06 14-57-32](https://user-images.githubusercontent.com/14224692/194429640-2c36a594-5614-497c-a167-c3d1fb2d6355.png)

