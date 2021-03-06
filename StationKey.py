"""
Stores dictionary all_stations that has
information for every BART station; such
as address, long, lat.
"""

all_stations = {'12TH': {'abbr': '12TH',
          'address': '1245 Broadway',
          'city': 'Oakland',
          'county': 'alameda',
          'gtfs_latitude': '37.803768',
          'gtfs_longitude': '-122.271450',
          'name': '12th St. Oakland City Center',
          'state': 'CA',
          'zipcode': '94612'},
 '16TH': {'abbr': '16TH',
          'address': '2000 Mission Street',
          'city': 'San Francisco',
          'county': 'sanfrancisco',
          'gtfs_latitude': '37.765062',
          'gtfs_longitude': '-122.419694',
          'name': '16th St. Mission',
          'state': 'CA',
          'zipcode': '94110'},
 '19TH': {'abbr': '19TH',
          'address': '1900 Broadway',
          'city': 'Oakland',
          'county': 'alameda',
          'gtfs_latitude': '37.808350',
          'gtfs_longitude': '-122.268602',
          'name': '19th St. Oakland',
          'state': 'CA',
          'zipcode': '94612'},
 '24TH': {'abbr': '24TH',
          'address': '2800 Mission Street',
          'city': 'San Francisco',
          'county': 'sanfrancisco',
          'gtfs_latitude': '37.752470',
          'gtfs_longitude': '-122.418143',
          'name': '24th St. Mission',
          'state': 'CA',
          'zipcode': '94110'},
 'ANTC': {'abbr': 'ANTC',
          'address': '1600 Slatten Ranch Road',
          'city': 'Antioch',
          'county': 'Contra Costa',
          'gtfs_latitude': '37.995388',
          'gtfs_longitude': '-121.780420',
          'name': 'Antioch',
          'state': 'CA',
          'zipcode': '94509'},
 'ASHB': {'abbr': 'ASHB',
          'address': '3100 Adeline Street',
          'city': 'Berkeley',
          'county': 'alameda',
          'gtfs_latitude': '37.852803',
          'gtfs_longitude': '-122.270062',
          'name': 'Ashby',
          'state': 'CA',
          'zipcode': '94703'},
 'BALB': {'abbr': 'BALB',
          'address': '401 Geneva Avenue',
          'city': 'San Francisco',
          'county': 'sanfrancisco',
          'gtfs_latitude': '37.721585',
          'gtfs_longitude': '-122.447506',
          'name': 'Balboa Park',
          'state': 'CA',
          'zipcode': '94112'},
 'BAYF': {'abbr': 'BAYF',
          'address': '15242 Hesperian Blvd.',
          'city': 'San Leandro',
          'county': 'alameda',
          'gtfs_latitude': '37.696924',
          'gtfs_longitude': '-122.126514',
          'name': 'Bay Fair',
          'state': 'CA',
          'zipcode': '94578'},
 'CAST': {'abbr': 'CAST',
          'address': '3301 Norbridge Dr.',
          'city': 'Castro Valley',
          'county': 'alameda',
          'gtfs_latitude': '37.690746',
          'gtfs_longitude': '-122.075602',
          'name': 'Castro Valley',
          'state': 'CA',
          'zipcode': '94546'},
 'CIVC': {'abbr': 'CIVC',
          'address': '1150 Market Street',
          'city': 'San Francisco',
          'county': 'sanfrancisco',
          'gtfs_latitude': '37.779732',
          'gtfs_longitude': '-122.414123',
          'name': 'Civic Center/UN Plaza',
          'state': 'CA',
          'zipcode': '94102'},
 'COLM': {'abbr': 'COLM',
          'address': '365 D Street',
          'city': 'Colma',
          'county': 'sanmateo',
          'gtfs_latitude': '37.684638',
          'gtfs_longitude': '-122.466233',
          'name': 'Colma',
          'state': 'CA',
          'zipcode': '94014'},
 'COLS': {'abbr': 'COLS',
          'address': '7200 San Leandro St.',
          'city': 'Oakland',
          'county': 'alameda',
          'gtfs_latitude': '37.753661',
          'gtfs_longitude': '-122.196869',
          'name': 'Coliseum',
          'state': 'CA',
          'zipcode': '94621'},
 'CONC': {'abbr': 'CONC',
          'address': '1451 Oakland Avenue',
          'city': 'Concord',
          'county': 'contracosta',
          'gtfs_latitude': '37.973737',
          'gtfs_longitude': '-122.029095',
          'name': 'Concord',
          'state': 'CA',
          'zipcode': '94520'},
 'DALY': {'abbr': 'DALY',
          'address': '500 John Daly Blvd.',
          'city': 'Daly City',
          'county': 'sanmateo',
          'gtfs_latitude': '37.706121',
          'gtfs_longitude': '-122.469081',
          'name': 'Daly City',
          'state': 'CA',
          'zipcode': '94014'},
 'DBRK': {'abbr': 'DBRK',
          'address': '2160 Shattuck Avenue',
          'city': 'Berkeley',
          'county': 'alameda',
          'gtfs_latitude': '37.870104',
          'gtfs_longitude': '-122.268133',
          'name': 'Downtown Berkeley',
          'state': 'CA',
          'zipcode': '94704'},
 'DELN': {'abbr': 'DELN',
          'address': '6400 Cutting Blvd.',
          'city': 'El Cerrito',
          'county': 'contracosta',
          'gtfs_latitude': '37.925086',
          'gtfs_longitude': '-122.316794',
          'name': 'El Cerrito del Norte',
          'state': 'CA',
          'zipcode': '94530'},
 'DUBL': {'abbr': 'DUBL',
          'address': '5801 Owens Dr.',
          'city': 'Pleasanton',
          'county': 'alameda',
          'gtfs_latitude': '37.701687',
          'gtfs_longitude': '-121.899179',
          'name': 'Dublin/Pleasanton',
          'state': 'CA',
          'zipcode': '94588'},
 'EMBR': {'abbr': 'EMBR',
          'address': '298 Market Street',
          'city': 'San Francisco',
          'county': 'sanfrancisco',
          'gtfs_latitude': '37.792874',
          'gtfs_longitude': '-122.397020',
          'name': 'Embarcadero',
          'state': 'CA',
          'zipcode': '94111'},
 'FRMT': {'abbr': 'FRMT',
          'address': '2000 BART Way',
          'city': 'Fremont',
          'county': 'alameda',
          'gtfs_latitude': '37.557465',
          'gtfs_longitude': '-121.976608',
          'name': 'Fremont',
          'state': 'CA',
          'zipcode': '94536'},
 'FTVL': {'abbr': 'FTVL',
          'address': '3401 East 12th Street',
          'city': 'Oakland',
          'county': 'alameda',
          'gtfs_latitude': '37.774836',
          'gtfs_longitude': '-122.224175',
          'name': 'Fruitvale',
          'state': 'CA',
          'zipcode': '94601'},
 'GLEN': {'abbr': 'GLEN',
          'address': '2901 Diamond Street',
          'city': 'San Francisco',
          'county': 'sanfrancisco',
          'gtfs_latitude': '37.733064',
          'gtfs_longitude': '-122.433817',
          'name': 'Glen Park',
          'state': 'CA',
          'zipcode': '94131'},
 'HAYW': {'abbr': 'HAYW',
          'address': "699 'B' Street",
          'city': 'Hayward',
          'county': 'alameda',
          'gtfs_latitude': '37.669723',
          'gtfs_longitude': '-122.087018',
          'name': 'Hayward',
          'state': 'CA',
          'zipcode': '94541'},
 'LAFY': {'abbr': 'LAFY',
          'address': '3601 Deer Hill Road',
          'city': 'Lafayette',
          'county': 'contracosta',
          'gtfs_latitude': '37.893176',
          'gtfs_longitude': '-122.124630',
          'name': 'Lafayette',
          'state': 'CA',
          'zipcode': '94549'},
 'LAKE': {'abbr': 'LAKE',
          'address': '800 Madison Street',
          'city': 'Oakland',
          'county': 'alameda',
          'gtfs_latitude': '37.797027',
          'gtfs_longitude': '-122.265180',
          'name': 'Lake Merritt',
          'state': 'CA',
          'zipcode': '94607'},
 'MCAR': {'abbr': 'MCAR',
          'address': '555 40th Street',
          'city': 'Oakland',
          'county': 'alameda',
          'gtfs_latitude': '37.829065',
          'gtfs_longitude': '-122.267040',
          'name': 'MacArthur',
          'state': 'CA',
          'zipcode': '94609'},
 'MLBR': {'abbr': 'MLBR',
          'address': '200 North Rollins Road',
          'city': 'Millbrae',
          'county': 'sanmateo',
          'gtfs_latitude': '37.600271',
          'gtfs_longitude': '-122.386702',
          'name': 'Millbrae',
          'state': 'CA',
          'zipcode': '94030'},
 'MONT': {'abbr': 'MONT',
          'address': '598 Market Street',
          'city': 'San Francisco',
          'county': 'sanfrancisco',
          'gtfs_latitude': '37.789405',
          'gtfs_longitude': '-122.401066',
          'name': 'Montgomery St.',
          'state': 'CA',
          'zipcode': '94104'},
 'NBRK': {'abbr': 'NBRK',
          'address': '1750 Sacramento Street',
          'city': 'Berkeley',
          'county': 'alameda',
          'gtfs_latitude': '37.873967',
          'gtfs_longitude': '-122.283440',
          'name': 'North Berkeley',
          'state': 'CA',
          'zipcode': '94702'},
 'NCON': {'abbr': 'NCON',
          'address': '3700 Port Chicago Highway',
          'city': 'Concord',
          'county': 'contracosta',
          'gtfs_latitude': '38.003193',
          'gtfs_longitude': '-122.024653',
          'name': 'North Concord/Martinez',
          'state': 'CA',
          'zipcode': '94520'},
 'OAKL': {'abbr': 'OAKL',
          'address': '4 Airport Drive',
          'city': 'Oakland',
          'county': 'alameda',
          'gtfs_latitude': '37.713238',
          'gtfs_longitude': '-122.212191',
          'name': 'Oakland International Airport',
          'state': 'CA',
          'zipcode': '94621'},
 'ORIN': {'abbr': 'ORIN',
          'address': '11 Camino Pablo',
          'city': 'Orinda',
          'county': 'contracosta',
          'gtfs_latitude': '37.878361',
          'gtfs_longitude': '-122.183791',
          'name': 'Orinda',
          'state': 'CA',
          'zipcode': '94563'},
 'PCTR': {'abbr': 'PCTR',
          'address': '2099 Railroad Avenue',
          'city': 'Pittsburg',
          'county': 'Contra Costa',
          'gtfs_latitude': '38.016941',
          'gtfs_longitude': '-121.889457',
          'name': 'Pittsburg Center',
          'state': 'CA',
          'zipcode': '94565'},
 'PHIL': {'abbr': 'PHIL',
          'address': '1365 Treat Blvd.',
          'city': 'Walnut Creek',
          'county': 'contracosta',
          'gtfs_latitude': '37.928468',
          'gtfs_longitude': '-122.056012',
          'name': 'Pleasant Hill/Contra Costa Centre',
          'state': 'CA',
          'zipcode': '94597'},
 'PITT': {'abbr': 'PITT',
          'address': '1700 West Leland Road',
          'city': 'Pittsburg',
          'county': 'contracosta',
          'gtfs_latitude': '38.018914',
          'gtfs_longitude': '-121.945154',
          'name': 'Pittsburg/Bay Point',
          'state': 'CA',
          'zipcode': '94565'},
 'PLZA': {'abbr': 'PLZA',
          'address': '6699 Fairmount Avenue',
          'city': 'El Cerrito',
          'county': 'contracosta',
          'gtfs_latitude': '37.902632',
          'gtfs_longitude': '-122.298904',
          'name': 'El Cerrito Plaza',
          'state': 'CA',
          'zipcode': '94530'},
 'POWL': {'abbr': 'POWL',
          'address': '899 Market Street',
          'city': 'San Francisco',
          'county': 'sanfrancisco',
          'gtfs_latitude': '37.784471',
          'gtfs_longitude': '-122.407974',
          'name': 'Powell St.',
          'state': 'CA',
          'zipcode': '94102'},
 'RICH': {'abbr': 'RICH',
          'address': '1700 Nevin Avenue',
          'city': 'Richmond',
          'county': 'contracosta',
          'gtfs_latitude': '37.936853',
          'gtfs_longitude': '-122.353099',
          'name': 'Richmond',
          'state': 'CA',
          'zipcode': '94801'},
 'ROCK': {'abbr': 'ROCK',
          'address': '5660 College Avenue',
          'city': 'Oakland',
          'county': 'alameda',
          'gtfs_latitude': '37.844702',
          'gtfs_longitude': '-122.251371',
          'name': 'Rockridge',
          'state': 'CA',
          'zipcode': '94618'},
 'SANL': {'abbr': 'SANL',
          'address': '1401 San Leandro Blvd.',
          'city': 'San Leandro',
          'county': 'alameda',
          'gtfs_latitude': '37.721947',
          'gtfs_longitude': '-122.160844',
          'name': 'San Leandro',
          'state': 'CA',
          'zipcode': '94577'},
 'SBRN': {'abbr': 'SBRN',
          'address': '1151 Huntington Avenue',
          'city': 'San Bruno',
          'county': 'sanmateo',
          'gtfs_latitude': '37.637761',
          'gtfs_longitude': '-122.416287',
          'name': 'San Bruno',
          'state': 'CA',
          'zipcode': '94066'},
 'SFIA': {'abbr': 'SFIA',
          'address': 'International Terminal, Level 3',
          'city': "San Francisco Int'l Airport",
          'county': 'sanmateo',
          'gtfs_latitude': '37.615966',
          'gtfs_longitude': '-122.392409',
          'name': 'San Francisco International Airport',
          'state': 'CA',
          'zipcode': '94128'},
 'SHAY': {'abbr': 'SHAY',
          'address': '28601 Dixon Street',
          'city': 'Hayward',
          'county': 'alameda',
          'gtfs_latitude': '37.634375',
          'gtfs_longitude': '-122.057189',
          'name': 'South Hayward',
          'state': 'CA',
          'zipcode': '94544'},
 'SSAN': {'abbr': 'SSAN',
          'address': '1333 Mission Road',
          'city': 'South San Francisco',
          'county': 'sanmateo',
          'gtfs_latitude': '37.664245',
          'gtfs_longitude': '-122.443960',
          'name': 'South San Francisco',
          'state': 'CA',
          'zipcode': '94080'},
 'UCTY': {'abbr': 'UCTY',
          'address': '10 Union Square',
          'city': 'Union City',
          'county': 'alameda',
          'gtfs_latitude': '37.590630',
          'gtfs_longitude': '-122.017388',
          'name': 'Union City',
          'state': 'CA',
          'zipcode': '94587'},
 'WARM': {'abbr': 'WARM',
          'address': '45193 Warm Springs Blvd',
          'city': 'Fremont',
          'county': 'alameda',
          'gtfs_latitude': '37.502171',
          'gtfs_longitude': '-121.939313',
          'name': 'Warm Springs/South Fremont',
          'state': 'CA',
          'zipcode': '94539'},
 'WCRK': {'abbr': 'WCRK',
          'address': '200 Ygnacio Valley Road',
          'city': 'Walnut Creek',
          'county': 'contracosta',
          'gtfs_latitude': '37.905522',
          'gtfs_longitude': '-122.067527',
          'name': 'Walnut Creek',
          'state': 'CA',
          'zipcode': '94596'},
 'WDUB': {'abbr': 'WDUB',
          'address': '6501 Golden Gate Drive',
          'city': 'Dublin',
          'county': 'alameda',
          'gtfs_latitude': '37.699756',
          'gtfs_longitude': '-121.928240',
          'name': 'West Dublin/Pleasanton',
          'state': 'CA',
          'zipcode': '94568'},
 'WOAK': {'abbr': 'WOAK',
          'address': '1451 7th Street',
          'city': 'Oakland',
          'county': 'alameda',
          'gtfs_latitude': '37.804872',
          'gtfs_longitude': '-122.295140',
          'name': 'West Oakland',
          'state': 'CA',
          'zipcode': '94607'}}