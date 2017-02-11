authorization_token = 'w_8PcNuhHa-y3xYdmc1x'
pagerduty_session = requests.Session()
pagerduty_session.headers.update({
  'Authorization': 'Token token=' + authorization_token,
  'Accept': 'application/vnd.pagerduty+json;version=2'
})

pagerduty_session.get('https://api.pagerduty.com/users')
