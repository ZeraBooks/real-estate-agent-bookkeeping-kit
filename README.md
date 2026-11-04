# Real estate agent bookkeeping kit

A real estate agent should run a separate business bank account, record each
commission at its gross amount with the brokerage split and fees as expenses,
log every business mile, and set money aside for quarterly estimated tax. This
kit has a chart of accounts, an expense category list, a commission split
check that ties each closing to the brokerage's deposit, a mileage log, and a
fictional agent's month.

## Files

| File | What it is |
|---|---|
| `chart-of-accounts.csv` | A starting chart for an agent or small team: checking, tax savings, card, owner draws, gross commission, split and fees, operating expenses. Columns: Number, Name, Type, Detail, Notes. |
| `expense-categories.csv` | Common agent costs and the account each one goes to, with notes on gifts, referral fees and personal spending. |
| `closings-october-2026.csv` | Two fictional closings: sale price, commission rate, your side, split rate, fees and the deposit received. |
| `check_closings.py` | Works out your side, the split and the expected deposit for each closing, ties it to the deposit, and prints the gross entry. |
| `october-2026-month.csv` | A fictional agent's October 2026: every line, its account, and whether it counts in profit. |
| `mileage-log-october-2026.csv` | The same month's trips: date, from, to, purpose, miles, and whether it is business or commuting. |
| `check_agent_month.py` | Prints the month's profit by section, lists draws and tax savings apart, and totals business miles. |

Both scripts are Python 3, standard library only.

## How to use it

1. Import `chart-of-accounts.csv` into your accounting software, or compare it
   with the accounts you have. Use `expense-categories.csv` when you are not
   sure where a cost goes.
2. For each closing, copy the figures from the commission statement or
   disbursement sheet into a file shaped like `closings-october-2026.csv` and
   run:

   ```
   python3 check_closings.py closings-october-2026.csv
   ```

   If the deposit doesn't tie, the commission statement has a deduction you
   haven't recorded yet.
3. Keep the mileage log as you drive, not in April. At month end run:

   ```
   python3 check_agent_month.py october-2026-month.csv mileage-log-october-2026.csv
   ```

## The worked month

Dana is a fictional agent paid through a brokerage on a 20% split with a
395.00 transaction fee per closing. Both October closings paid 5% in total,
shared equally between the listing and buyer's agents.

| Closing | Your side | Split (20%) | Transaction fee | Other | Deposit |
|---|---|---|---|---|---|
| 14 Alder Court, listing side, 480,000.00 | 12,000.00 | 2,400.00 | 395.00 | 0.00 | 9,205.00 |
| 2207 Harbor View Drive, buyer side, 615,000.00 | 15,375.00 | 3,075.00 | 395.00 | 50.00 E&O fee | 11,855.00 |
| **Total** | **27,375.00** | **5,475.00** | **790.00** | **50.00** | **21,060.00** |

Both deposits tie. Booking only the deposits would hide 6,315.00 of costs.

October, booked gross:

| | Amount |
|---|---|
| Gross commission income | 27,375.00 |
| Referral fees received | 1,500.00 |
| **Revenue** | **28,875.00** |
| Brokerage split | 5,475.00 |
| Transaction fees | 790.00 |
| **Cost of revenue** | **6,265.00** |
| Desk fee | 500.00 |
| MLS dues | 145.00 |
| E&O fee | 50.00 |
| Marketing: listing photos and signs | 530.00 |
| Lead generation | 450.00 |
| Vehicle: fuel | 212.40 |
| Client gifts, 3 buyers at 120.00 | 360.00 |
| Continuing education | 199.00 |
| Phone and CRM | 129.00 |
| **Operating expenses** | **2,575.40** |
| **Profit** | **20,034.60** |

Dana also moved 6,000.00 to tax savings and took a 5,000.00 owner draw. Neither
is an expense, so neither is in profit.

The three closing gifts are booked at their full 360.00 with each buyer's name
in the memo. The IRS limits the deduction to $25 per person per year (IRS
Publication 463), so 75.00 is deductible. Your tax preparer applies the limit.

The mileage log shows 183 business miles: showings, an open house, a listing
appointment, the inspection and appraisal, the two closings and placing a
listing sign. The 18 miles from home to the brokerage office on regular office
days are commuting and are left out.

The agent, properties and figures are fictional.

## FAQ

### Is a real estate agent self-employed for taxes?

Almost always. The IRS treats licensed real estate agents as self-employed for
federal tax purposes when nearly all their pay comes from sales and a written
contract says they aren't employees. No tax is withheld from commissions, and
the brokerage reports what it paid on Form 1099-NEC.

### Should I record my commission gross or net?

Gross. Record your side of the commission as income and the brokerage split
and fees as expenses. Profit comes out the same either way, but gross books
show what the brokerage costs you and match the 1099-NEC whichever way it is
reported.

### When is estimated tax due?

For 2026 income: April 15, June 15 and September 15, 2026, and January 15,
2027. On top of income tax, self-employment tax is 15.3% (12.4% Social
Security, 2.9% Medicare) once net earnings reach $400. Your tax preparer sets
the amounts; current books tell them the profit so far.

## Learn more

Full guide: [Bookkeeping for real estate agents](https://www.zerabooks.com/bookkeeping-for-real-estate-agents). Related: [ZeraBooks bookkeeping services](https://www.zerabooks.com/bookkeeping-services).

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). Free to use and adapt with credit to ZeraBooks.
The code (`*.py`) is licensed under [MIT](LICENSE-CODE).

Maintained by [ZeraBooks](https://www.zerabooks.com).
