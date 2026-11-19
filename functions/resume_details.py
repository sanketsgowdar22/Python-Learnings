def resume_details(name,degree,yop=None,*skills,**results):
    print(f"Name : {name}")
    print(f"Degree : {degree}")
    print(f"Passed Out in : {yop}")
    print(f"Skills are :{skills}") 
    print(f"Results are as follows: {results}")
    
resume_details("Sanket","B.E",2026,"Python","HTML","CSS","SQL","MySQL",SSLC=81.20,PUC=73.83,BE=8.61)
