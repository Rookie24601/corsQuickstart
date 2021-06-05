
# To configure         
1. Create a GCS bucket called corstest123.         
`gsutil mb -c standard -b on gs://corstest123`       
`-b on` argument makes the bucket access uniform.           

2. Create `cors_config.json` file.              
```
[
    {
        "maxAgeSeconds": 60, 
        "method": ["GET", "OPTIONS"], 
        "origin": ["http://test.example.com", "http://127.0.0.1:5000"], 
        "responseHeader": ["Content-Type"]
    }
]
```           

3. Enable CORS on the bucket         
`gsutil cors get gs://corstest123`             
`gsutil cors set cors_config.json gs://corstest123`           
`gsutil cors get gs://corstest123`   

4. Upload some test objects to the bucket          
`gsutil cp -r 'testObjects/*.*' gs://corstest123`           

5. Make the bucket public        
`gsutil iam ch allUsers:objectViewer gs://corstest123`      

<br/><br/>  

# To run       
## On powershell        
`$env:FLASK_APP = "main.py"`        
`$env:FLASK_ENV = "development"`       
`flask run`   OR `flask run --port 4000`        

You can print its values with `$env:[ENV_VARIABLE_NAME]`          
Example:     `$env:FLASK_APP`        
<br/>
## On linux       
`export FLASK_APP="main.py"`       
`export FLASK_ENV="development"`       
`flask run`   OR `flask run --port 4000`        

You can print its values with `echo $[ENV_VARIABLE_NAME]`          
Example:     `echo $FLASK_APP`        
<br/>
## Personal Notes           
1. Check the code in `index.html`and limit **only** to replace the values of the bucket and object names.          

2. For every update of the CORS configuration in the bucket, **wait one minute** before requesting the object since the bucket has a MAX_AGE of 60 seconds.    
Not waiting enough could result in false positives which could further result in assuming that the code from index.html is not working. 

3. Keep in mind that requests to the JSON API will always succeed(regardless of the CORS configuration).    
This behavior is documented [here](https://cloud.google.com/storage/docs/cross-origin#server-side-support).            

4. Valid GCS API endpoints can be found [here](https://cloud.google.com/storage/docs/request-endpoints#typical).     
You can always refer to the docs to validate that the code in `index.html` is up to date.      

5. Have fun!      
You can check that CORS works only with the XML API by commenting and uncommenting the variable `url_template`.        
You can check that the XML API only allows cross-scripting to the origins defined in `cors_config.json` by running the flask application with different ports; `cors_config.json` content only allows flask apps that run in port 5000 to cross script; changing the running port and then calling the `/api` endpoint should produce a cors error.        



