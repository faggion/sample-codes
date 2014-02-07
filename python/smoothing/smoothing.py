# coding: utf-8

import logging, sys, os, traceback
import argparse


def get_max_bid_price(base, time_start, time_now, time_end,
                      budget_start, budget_now, budget_end):
    ideal_velocity = ( budget_end - budget_start ) / ( time_end - time_start )
    logging.debug("ideal velocity   = %.8f" % ideal_velocity)
    ideal_digest   = ( budget_start + ideal_velocity * ( time_now - time_start) )
    logging.debug("ideal digest     = %.8f" % ideal_digest)
    remaining_budget = ideal_digest - budget_now
    logging.debug("remaining budget = %.8f" % remaining_budget)
    if base < remaining_budget:
        return base
    return remaining_budget

def main():
    logging.getLogger().setLevel(logging.DEBUG)
    parser = argparse.ArgumentParser(description='calc smoothing')
    parser.add_argument('-p', '--price',        required=True, type=int, help="price")
    parser.add_argument('-t', '--time-start',   required=True, type=int, help="t0")
    parser.add_argument('-T', '--time-now',     required=True, type=int, help="tx")
    parser.add_argument('-e', '--time-end',     required=True, type=int, help="te")
    parser.add_argument('-b', '--budget-start', required=True, type=int, help="t0")
    parser.add_argument('-B', '--budget-now',   required=True, type=int, help="tx")
    parser.add_argument('-E', '--budget-end',   required=True, type=int, help="te")
    a = parser.parse_args()
    max_bid_price = get_max_bid_price(a.price, a.time_start, a.time_now, a.time_end, a.budget_start, a.budget_now, a.budget_end)
    logging.debug("max bid price    = %.8f" % max_bid_price)

if __name__ == '__main__':
    main()


"""

% python smoothing.py --price=1000 --time-start=100 --time-now=115 --time-end=120 --budget-start=10 --budget-end=30 --budget-now=12
DEBUG:root:ideal velocity   = 1.00000000
DEBUG:root:ideal digest     = 25.00000000
DEBUG:root:remaining budget = 13.00000000
DEBUG:root:max bid price    = 13.00000000
% python smoothing.py --price=1000 --time-start=100 --time-now=115 --time-end=120 --budget-start=10 --budget-end=30 --budget-now=15
DEBUG:root:ideal velocity   = 1.00000000
DEBUG:root:ideal digest     = 25.00000000
DEBUG:root:remaining budget = 10.00000000
DEBUG:root:max bid price    = 10.00000000
% python smoothing.py --price=1000 --time-start=100 --time-now=115 --time-end=120 --budget-start=10 --budget-end=30 --budget-now=8
DEBUG:root:ideal velocity   = 1.00000000
DEBUG:root:ideal digest     = 25.00000000
DEBUG:root:remaining budget = 17.00000000
DEBUG:root:max bid price    = 17.00000000
% python smoothing.py --price=1000 --time-start=100 --time-now=105 --time-end=120 --budget-start=10 --budget-end=30 --budget-now=12
DEBUG:root:ideal velocity   = 1.00000000
DEBUG:root:ideal digest     = 15.00000000
DEBUG:root:remaining budget = 3.00000000
DEBUG:root:max bid price    = 3.00000000
% python smoothing.py --price=1000 --time-start=100 --time-now=105 --time-end=120 --budget-start=10 --budget-end=30 --budget-now=15
DEBUG:root:ideal velocity   = 1.00000000
DEBUG:root:ideal digest     = 15.00000000
DEBUG:root:remaining budget = 0.00000000
DEBUG:root:max bid price    = 0.00000000
% python smoothing.py --price=1000 --time-start=100 --time-now=105 --time-end=120 --budget-start=10 --budget-end=30 --budget-now=8
DEBUG:root:ideal velocity   = 1.00000000
DEBUG:root:ideal digest     = 15.00000000
DEBUG:root:remaining budget = 7.00000000
DEBUG:root:max bid price    = 7.00000000

"""
