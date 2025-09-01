# Write your MySQL query statement below
SELECT 
    tweet_id 
FROM 
    Tweets
WHERE 
# in sql there is LENGTH and char_length , lenght gives the num of output bytes in a strong and char_length gives num of char in a string.
    CHAR_LENGTH(content) > 15