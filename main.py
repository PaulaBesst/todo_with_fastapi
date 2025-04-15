from fastapi import FastAPI


#create instance of fastapi
app = FastAPI()

#add a path operation decorate
@app.get('/')
def index():        #function
    return {'data':{'name':"Paula"}}  #important to return something


@app.get('/about')
def about():
    return {'data':'about page'}