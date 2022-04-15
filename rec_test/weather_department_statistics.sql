-- FINAL SUBMISSION

SELECT DISTINCT state.name, country.name,
    CASE 
        WHEN state_weather_stats.record_date BETWEEN '2018-11-01' AND '2018-11-30' THEN AVG(state_weather_stats.humidity) 
    END AS average_monthly_humidity,
    
    CASE
        WHEN state_weather_stats.record_date BETWEEN '2018-11-01' AND '2018-11-30' AND state_weather_stats.temperature < 15 THEN 'COLD' 
        -- WHEN state_weather_stats.record_date BETWEEN '2018-11-01' AND '2018-11-30' AND 15 >= state_weather_stats.temperature < 30 THEN 'WARM' 
        WHEN state_weather_stats.record_date BETWEEN '2018-11-01' AND '2018-11-30' AND state_weather_stats.temperature >= 30 THEN 'HOT' 
    END AS weather_type

FROM state, country, state_weather_stats

WHERE state.id = state_weather_stats.state_id
    AND country.id = state.country_id

GROUP BY state.name, country.name, state_weather_stats.record_date, state_weather_stats.humidity, state_weather_stats.temperature
ORDER BY average_monthly_humidity DESC, state.name;

-- #######################################

-- full test case for practice: 

-- Idaho United States 43.0333 WARM
-- South Dakota United States 42.6333 WARM
-- Nord Cameroon 41.5333 WARM
-- Adamaoua Cameroon 41.1333 WARM
-- Sud-Ouest Cameroon 40.5000 WARM
-- Kansas United States 40.3333 WARM
-- North Dakota United States 40.1667 WARM
-- Saskatchewan Canada 39.7000 WARM
-- North Carolina United States 39.5333 WARM
-- Ontario Canada 39.4000 WARM
-- Virginia United States 39.4000 COLD
-- Iowa United States 39.3667 WARM
-- Vastmanlands Sweden 39.3000 WARM
-- Alaska United States 39.2333 WARM
-- Kalmar Sweden 39.2333 WARM
-- Camaguey Cuba 39.1000 WARM
-- Nord-Ouest Cameroon 38.8000 WARM
-- Ohio United States 38.8000 WARM
-- New Mexico United States 38.7667 WARM
-- Montana United States 38.7333 WARM
-- West Virginia United States 38.6667 WARM
-- Ciego de Avila Cuba 38.6000 WARM
-- Hallands Sweden 38.6000 WARM
-- Manitoba Canada 38.6000 WARM
-- Ostergotlands Sweden 38.5667 WARM
-- Nevada United States 38.5333 WARM
-- Rhode Island United States 38.5333 WARM
-- La Habana Cuba 38.2333 WARM
-- Oregon United States 38.2000 WARM
-- Arkansas United States 38.0667 WARM
-- Vasternorrlands Sweden 38.0333 WARM
-- Jamtlands Sweden 37.9667 WARM
-- New York United States 37.9333 WARM
-- Dalarnas Sweden 37.8333 WARM
-- New Hampshire United States 37.8333 WARM
-- Sud Cameroon 37.8000 WARM
-- Jonkopings Sweden 37.5667 WARM
-- Northwest Territories Canada 37.5333 WARM
-- Ouest Cameroon 37.5333 WARM
-- Alberta Canada 37.5000 WARM
-- Nunavut Canada 37.4667 WARM
-- Matanzas Cuba 37.4000 WARM
-- Connecticut United States 37.3000 WARM
-- Louisiana United States 37.2667 WARM
-- Ciudad de La Habana Cuba 37.2333 WARM
-- Sodermanlands Sweden 37.1667 WARM
-- Gotlands Sweden 37.1000 WARM
-- Varmlands Sweden 37.0333 WARM
-- Pennsylvania United States 36.7667 WARM
-- Texas United States 36.7333 WARM
-- Florida United States 36.7000 WARM
-- Kentucky United States 36.7000 WARM
-- Extreme-Nord Cameroon 36.6333 WARM
-- Villa Clara Cuba 36.5333 WARM
-- Illinois United States 36.5000 WARM
-- Santiago de Cuba Cuba 36.5000 WARM
-- Vasterbottens Sweden 36.4667 WARM
-- British Columbia Canada 36.3667 WARM
-- District of Columbia United States 36.3333 WARM
-- New Brunswick Canada 36.3000 WARM
-- Minnesota United States 36.2667 WARM
-- Alabama United States 36.2333 WARM
-- Indiana United States 36.2000 WARM
-- Littoral Cameroon 36.1000 WARM
-- Washington United States 36.1000 WARM
-- Colorado United States 36.0333 WARM
-- Isla de la Juventud Cuba 35.9333 WARM
-- Newfoundland and Labrador Canada 35.9333 WARM
-- Kronobergs Sweden 35.9000 WARM
-- Las Tunas Cuba 35.8000 WARM
-- Vermont United States 35.5000 COLD
-- New Jersey United States 35.4667 WARM
-- Cienfuegos Cuba 35.3667 WARM
-- Maryland United States 35.3000 WARM
-- Nebraska United States 35.3000 WARM
-- Mississippi United States 34.9000 WARM
-- California United States 34.6333 WARM
-- Hawaii United States 34.6000 WARM
-- Orebro Sweden 34.6000 WARM
-- Oklahoma United States 34.5333 WARM
-- Nova Scotia Canada 34.4667 WARM
-- Gavleborgs Sweden 34.4333 WARM
-- Stockholms Sweden 34.4000 WARM
-- Uppsala Sweden 34.2667 WARM
-- Guantanamo Cuba 34.2333 WARM
-- Tennessee United States 34.1333 WARM
-- Norrbottens Sweden 34.0333 WARM
-- Missouri United States 33.9667 WARM
-- Utah United States 33.9667 WARM
-- Massachusetts United States 33.8000 WARM
-- Blekinge Sweden 33.7667 WARM
-- Quebec Canada 33.6333 WARM
-- Delaware United States 33.5667 WARM
-- Granma Cuba 33.4333 WARM
-- Skane Sweden 33.4000 WARM
-- Arizona United States 33.2667 WARM
-- Est Cameroon 33.2333 WARM
-- Pinar del Rio Cuba 33.2000 WARM
-- Michigan United States 33.1333 WARM
-- Maine United States 33.0667 WARM
-- Wyoming United States 33.0667 WARM
-- Georgia United States 33.0333 WARM
-- Vastra Gotalands Sweden 32.9000 WARM
-- Wisconsin United States 32.9000 WARM
-- Sancti Spiritus Cuba 32.7667 WARM
-- Prince Edward Island Canada 32.6333 WARM
-- Yukon Territory Canada 32.0000 WARM
-- Centre Cameroon 31.3667 COLD
-- South Carolina United States 30.8000 WARM
-- Holguin Cuba 26.8333 WARM


-- ##################
-- test results:

-- -- Your Output (stdout)
-- Alabama United States 60.0000 WARM
-- Alaska United States 60.0000 COLD
-- Blekinge Sweden 60.0000 COLD
-- Camaguey Cuba 60.0000 WARM
-- Ciego de Avila Cuba 60.0000 WARM
-- Ciudad de La Habana Cuba 60.0000 COLD
-- Connecticut United States 60.0000 COLD
-- District of Columbia United States 60.0000 WARM
-- Georgia United States 60.0000 WARM
-- Gotlands Sweden 60.0000 WARM
-- Idaho United States 60.0000 WARM
-- Illinois United States 60.0000 COLD
-- Iowa United States 60.0000 COLD
-- Isla de la Juventud Cuba 60.0000 WARM
-- Jonkopings Sweden 60.0000 WARM
-- Kentucky United States 60.0000 WARM
-- Kentucky United States 60.0000 COLD
-- La Habana Cuba 60.0000 COLD
-- Massachusetts United States 60.0000 WARM
-- Minnesota United States 60.0000 WARM
-- Minnesota United States 60.0000 COLD
-- Nevada United States 60.0000 COLD
-- Nevada United States 60.0000 WARM
-- New Brunswick Canada 60.0000 WARM
-- New York United States 60.0000 COLD
-- Nord Cameroon 60.0000 WARM
-- Nord Cameroon 60.0000 COLD
-- North Carolina United States 60.0000 COLD
-- North Dakota United States 60.0000 COLD
-- Northwest Territori{-truncated-}

-- Expected Output
-- Idaho United States 43.0333 WARM
-- South Dakota United States 42.6333 WARM
-- Nord Cameroon 41.5333 WARM
-- Adamaoua Cameroon 41.1333 WARM
-- Sud-Ouest Cameroon 40.5000 WARM
-- Kansas United States 40.3333 WARM
-- North Dakota United States 40.1667 WARM
-- Saskatchewan Canada 39.7000 WARM
-- North Carolina United States 39.5333 WARM
-- Ontario Canada 39.4000 WARM
-- Virginia United States 39.4000 COLD
-- Iowa United States 39.3667 WARM
-- Vastmanlands Sweden 39.3000 WARM
-- Alaska United States 39.2333 WARM
-- Kalmar Sweden 39.2333 WARM
-- Camaguey Cuba 39.1000 WARM
-- Nord-Ouest Cameroon 38.8000 WARM
-- Ohio United States 38.8000 WARM
-- New Mexico United States 38.7667 WARM
-- Montana United States 38.7333 WARM
-- West Virginia United States 38.6667 WARM
-- Ciego de Avila Cuba 38.6000 WARM
-- Hallands Sweden 38.6000 WARM
-- Manitoba Canada 38.6000 WARM
-- Ostergotlands Sweden 38.5667 WARM
-- Nevada United States 38.5333 WARM
-- Rhode Island United States 38.5333 WARM
-- La Habana Cuba 38.2333 WARM
-- Oregon United States 38.2000 WARM
-- Arkansas United States 38.0667 WARM
-- Vasternorrlands Swed{-truncated-}