import requests
import psycopg2

conn = psycopg2.connect(database='NHL', user='postgres', password='postgres', host='localhost', port='5432')

req = requests.get('http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22playerName%22,%22direction%22:%22ASC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20172018%20and%20seasonId%3C=20172018')
data = req.json()['data']

my_data = []
for item in data:
    season = item['seasonId']
    player = item['playerName']
    first_name = item['playerFirstName']
    last_Name = item['playerLastName']
    playerId = item['playerId']
    height = item['playerHeight']
    pos = item['playerPositionCode']
    handed = item['playerShootsCatches']
    city = item['playerBirthCity']
    country = item['playerBirthCountry']
    state = item['playerBirthStateProvince']
    dob = item['playerBirthDate']
    draft_year = item['playerDraftYear']
    draft_round = item['playerDraftRoundNo']
    draft_overall = item['playerDraftOverallPickNo']
    my_data.append([playerId, player, first_name, last_Name, height, pos, handed, city, country, state, dob, draft_year, draft_round, draft_overall, season])

cur = conn.cursor()
cur.execute("CREATE TABLE t_skaters (data json);")
cur.executemany("INSERT INTO t_skaters VALUES (%s)", (my_data,))