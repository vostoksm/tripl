"""Return the airports fitted to budget from Amazon dynamoDb"""
import boto3

def get_airports(origin, remaining_budget, month):
    """
    Return the airports fitted to budget from Amazon dynamoDb
    Input arguments:
    origin -- departure airport
    remaining_budget -- maximal budget to be spent on flight
    month -- month of travel
    Output:
    List of valid airports
    """
    pass
