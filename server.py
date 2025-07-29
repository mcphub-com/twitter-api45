import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/alexanderxbx/api/twitter-api45'

mcp = FastMCP('twitter-api45')

@mcp.tool()
def user_info(screenname: Annotated[str, Field(description='')],
              rest_id: Annotated[Union[str, None], Field(description="Twitter user's id. This parameter overwrites screenname parameter.")] = None) -> dict: 
    '''Using this method you can get information about user by the screenname.'''
    url = 'https://twitter-api45.p.rapidapi.com/screenname.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'screenname': screenname,
        'rest_id': rest_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_timeline(screenname: Annotated[str, Field(description='')],
                  rest_id: Annotated[Union[str, None], Field(description='Optional parameter that overwrites the screename. Screename could be a random string if this user id is passed.')] = None,
                  cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint gets lates user's tweets by it's screenname.'''
    url = 'https://twitter-api45.p.rapidapi.com/timeline.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'screenname': screenname,
        'rest_id': rest_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def following(screenname: Annotated[str, Field(description='')],
              cursor: Annotated[Union[str, None], Field(description='')] = None,
              rest_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get the list of accounts user is following.'''
    url = 'https://twitter-api45.p.rapidapi.com/following.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'screenname': screenname,
        'cursor': cursor,
        'rest_id': rest_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def followers(screenname: Annotated[str, Field(description='')],
              cursor: Annotated[Union[str, None], Field(description='')] = None,
              blue_verified: Annotated[Literal['0', '1', None], Field(description='')] = None) -> dict: 
    '''Get latest user's followers list'''
    url = 'https://twitter-api45.p.rapidapi.com/followers.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'screenname': screenname,
        'cursor': cursor,
        'blue_verified': blue_verified,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_info(id: Annotated[str, Field(description='')]) -> dict: 
    '''With this endpoint you can get tweet info by it's id.'''
    url = 'https://twitter-api45.p.rapidapi.com/tweet.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def affilates(screenname: Annotated[str, Field(description='')],
              cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Give you the list of affilates for the corporate account.'''
    url = 'https://twitter-api45.p.rapidapi.com/affilates.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'screenname': screenname,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_smedia(screenname: Annotated[str, Field(description='')],
                rest_id: Annotated[Union[str, None], Field(description='')] = None,
                cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Helps to get a user's media'''
    url = 'https://twitter-api45.p.rapidapi.com/usermedia.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'screenname': screenname,
        'rest_id': rest_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def retweets(id: Annotated[str, Field(description='')],
             cursor: Annotated[Union[str, None], Field(description='The value of the next_cursor field in the response. Example value: HBaE2pGdj9GLqjEAAA==')] = None) -> dict: 
    '''Get the list of of users who retweeted the tweet.'''
    url = 'https://twitter-api45.p.rapidapi.com/retweets.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def trends(country: Annotated[Literal['UnitedStates', 'China', 'India', 'Japan', 'Russia', 'Germany', 'Indonesia', 'Brazil', 'France', 'UnitedKingdom', 'Turkey', 'Italy', 'Mexico', 'SouthKorea', 'Canada', 'Spain', 'SaudiArabia', 'Egypt', 'Australia', 'Poland', 'Iran', 'Pakistan', 'Vietnam', 'Nigeria', 'Bangladesh', 'Netherlands', 'Argentina', 'Philippines', 'Malaysia', 'Columbia', 'UnitedArabEmirates', 'Romania', 'Belgium', 'Switzerland', 'Singapore', 'Sweden', 'Norway', 'Austria', 'Kazakhstan', 'Algeria', 'Chile', 'Czechia', 'Peru', 'Iraq', 'Israel', 'Ukraine', 'Denmark', 'Portugal', 'Hungary', 'Greece', 'Finland', 'NewZealand', 'Bulgaria', 'Belarus', 'Slovakia', 'Serbia', 'Lithuania', 'Luxembourg', 'Estonia'], Field(description='')]) -> dict: 
    '''Please let me know if you need other countries in the list.'''
    url = 'https://twitter-api45.p.rapidapi.com/trends.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(query: Annotated[str, Field(description='')],
           cursor: Annotated[Union[str, None], Field(description='')] = None,
           search_type: Annotated[Literal['Top', 'Latest', 'Media', 'People', 'Lists', None], Field(description='')] = None) -> dict: 
    '''WARNING: The Search endpoint is rate limited for new customers to 60 requests/minute. Please contact me if you need a higher limit. Email: alexander.xbx@gmail.com'''
    url = 'https://twitter-api45.p.rapidapi.com/search.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'cursor': cursor,
        'search_type': search_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def check_retweet(screenname: Annotated[str, Field(description='')],
                  tweet_id: Annotated[str, Field(description='')]) -> dict: 
    '''This endpoint get latest tweets of the user and checks if there is a retweet of the needed tweet. WARNING: might not be suitable for old retweets.'''
    url = 'https://twitter-api45.p.rapidapi.com/checkretweet.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'screenname': screenname,
        'tweet_id': tweet_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_replies(screenname: Annotated[str, Field(description='')],
                 cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Gets user's replies of the user.'''
    url = 'https://twitter-api45.p.rapidapi.com/replies.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'screenname': screenname,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_thread(id: Annotated[str, Field(description='')],
                 cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Gets the basic tweet info and the replies to it.'''
    url = 'https://twitter-api45.p.rapidapi.com/tweet_thread.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def latest_replies(id: Annotated[str, Field(description='')],
                   cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Gets the latest replies of the tweet.'''
    url = 'https://twitter-api45.p.rapidapi.com/latest_replies.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def check_follow(user: Annotated[str, Field(description='')],
                 follows: Annotated[str, Field(description='')]) -> dict: 
    '''This endpoint get latest subscriptins of the user and latest followers for the target account. And checks if user follows the needed account. WARNING: might not be suitable for big accounts or old subscriptions.'''
    url = 'https://twitter-api45.p.rapidapi.com/checkfollow.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'follows': follows,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_timeline(list_id: Annotated[str, Field(description='')],
                  cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''With this endpoint you can get the timeline of the lists.'''
    url = 'https://twitter-api45.p.rapidapi.com/listtimeline.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list_id': list_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def communities_posts_search_latest(query: Annotated[str, Field(description='')],
                                    cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for the Latest posts in communities'''
    url = 'https://twitter-api45.p.rapidapi.com/search_communities_latest.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def communities_posts_search_top(query: Annotated[str, Field(description='')],
                                 cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for the posts in communities post order top.'''
    url = 'https://twitter-api45.p.rapidapi.com/search_communities_top.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def communities_search(query: Annotated[str, Field(description='')],
                       cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for the communities on the X'''
    url = 'https://twitter-api45.p.rapidapi.com/search_communities.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def profiles_by_restids(rest_ids: Annotated[str, Field(description='')]) -> dict: 
    '''Returns an array of users by their rest_ids.'''
    url = 'https://twitter-api45.p.rapidapi.com/screennames.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'rest_ids': rest_ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def comunity_posts(community_id: Annotated[str, Field(description='')],
                   cursor: Annotated[Union[str, None], Field(description='')] = None,
                   ranking: Annotated[Literal['Top', 'Latest', None], Field(description='')] = None) -> dict: 
    '''Returns the posts from the community.'''
    url = 'https://twitter-api45.p.rapidapi.com/community_timeline.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'community_id': community_id,
        'cursor': cursor,
        'ranking': ranking,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_followers(list_id: Annotated[str, Field(description='')],
                   cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get the followers of the list on Twitter / X'''
    url = 'https://twitter-api45.p.rapidapi.com/list_followers.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list_id': list_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_members(list_id: Annotated[str, Field(description='')],
                 cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get the members of the list on Twitter / X'''
    url = 'https://twitter-api45.p.rapidapi.com/list_members.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list_id': list_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def spaces_info(id: Annotated[str, Field(description='')]) -> dict: 
    '''Give you the basic information about the spaces.'''
    url = 'https://twitter-api45.p.rapidapi.com/spaces.php'
    headers = {'x-rapidapi-host': 'twitter-api45.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
