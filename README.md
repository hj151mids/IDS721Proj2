# IDS721Proj2 Kubernetes Based Continuous Delivery
A simple webapp to test whether a number is a prime number is first built in the Cloud9 environment.  
Then to containerize it, I built the docker image and pushed to the ECR repository for public access.  
You should follow the push commands provided to you by ECR.  
![image](https://user-images.githubusercontent.com/90075179/155903627-d7b55c8b-6910-49b1-bea4-8f14a04ba175.png)
The image url is : public.ecr.aws/k2l3c8y7/ids721proj2demo4:latest  
Anyone can run docker pull in their AWS CLI to run this project.  
![image](https://user-images.githubusercontent.com/90075179/155903386-b89f5a7a-959a-4f88-bb62-441ec6dc30d4.png)
For the continuous integration of the project, I used Github Actions to continuously test each git push.  
To realize the continuous delivery of the project on a Kubernete based service, I used AWS's apprunner to deploy my code.  
This is convenient because users can type the url in their browser and interact with my webapp.  
![image](https://user-images.githubusercontent.com/90075179/155903462-cca076ab-5119-4dab-b9db-493d3dc01d76.png)
The url is https://vpx4wbani2.us-east-2.awsapprunner.com for accessing the welcome page and https://vpx4wbani2.us-east-2.awsapprunner.com/is_prime/12 for accessing the is_prime function. I will have to shut down the apprunner service to save money, so one should use docker pull the container and deploy to their own apprunner to test it out.  
To show that the apprunner is actually working, here are two screenshots:  
![image](https://user-images.githubusercontent.com/90075179/155903544-def27b37-35df-46f2-89c2-687272d51ca0.png)
![image](https://user-images.githubusercontent.com/90075179/155903548-bbf4efd5-93ec-43a3-8149-bf2817035b6a.png)
