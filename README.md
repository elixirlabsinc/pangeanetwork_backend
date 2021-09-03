Pangea Network Admin Dashboard - Backend

To view latest staging version, visit [https://pangea-backend.herokuapp.com/](https://pangea-backend.herokuapp.com/)


# To run this code locally:

1. Clone the repository:

    `git clone https://github.com/elixirlabsinc/pangeanetwork.git`
    
    `cd pangeanetwork`
    
## Backend setup

2. Create and activate a virtual environment:

    `virtualenv env -p python3`
    
    `source env/bin/activate`

3. Install requirements:

    `pip install -r 'requirements.txt'`

4. Run the application:

    `gunicorn 'app:create_app()'`
        
 
 ## Frontend setup
 
 5. To run the frontend, see [pangea network frontend codebase](https://github.com/elixirlabsinc/pangeanetwork)



## Testing with Africa's Talking API

1. Install [ngrok](https://ngrok.com/download)

2. With backend server running, run `./ngrok http 5000` in a new tab

3. From your Africa's Talking account, navigate to SMS > SMS Callback URLs > Incoming Messages and fill in the forwarding url from ngrok in the URL form.

4. From your Africa's Talking account, navigate to Settings > API Key to generate an API Key. Store this in your local environment variables as `AT_API_KEY`.

5. Open the Sandbox by clicking on `Launch Simulator` from your Africa's Talking account and there you can test sending/receiving SMS messages to/from your local running instance of the app.



## Contributing

If you see an open issue you want to work on, either assign it to yourself or comment that you are starting to work on it. Check out a new branch from master with the ticket number and a brief description of the ticket such as `[ticket number]_add_transactions_endpoint`. Once you have finished your changes, push them to your remote branch and open up a Merge Request back to the master branch. 
