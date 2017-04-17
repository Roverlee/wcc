#code from chuck severance who said he probly took it off stackoverflow ;)
import urllib
import oauth2 as oauth
import hidden

#it augments the url you provide with all the signature that twitter wants,
#with google geojson, we just had to augment the url with the right phrasing,
#we didnt have to additionally augment like we do here with an authorization signature because they limit by rate, not by signature it seems
#parameters is  a dictionary
def augment (url, parameters) :
    secrets = hidden.oauth()
    #I removed the Oauth before the Consumer Token etc to make it work on mine..
    consumer = oauth.Consumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.Token(secrets['token_key'], secrets['token_secret'])
    oauth_request = oauth.Request.from_consumer_and_token(consumer,
        token=token, http_method='GET', http_url=url, parameters=parameters)
    oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()
