"""Profit for an agent's month, plus the mileage log total.

The month file has one line per item booked, with its account number and
whether it counts in profit. Revenue is the 40000s, cost of revenue the
50000s, operating expenses the 60000s. Transfers to tax savings, owner draws
and estimated tax payments are listed apart because they are not expenses.

The mileage log has one row per trip. Business trips are totaled by purpose;
commuting rows (Business = No) are left out.

Usage: python3 check_agent_month.py october-2026-month.csv mileage-log-october-2026.csv
Python 3, standard library only.
"""
import csv
import sys
from decimal import Decimal

SECTIONS = {"4": "Revenue", "5": "Cost of revenue", "6": "Operating expenses"}


def d(cell):
    return Decimal(cell.strip().replace(",", "")) if cell and cell.strip() else Decimal("0")


def main(month_path, miles_path):
    ok = True
    by_section = {k: {} for k in SECTIONS.values()}
    outside = []
    gifts = Decimal(0)
    with open(month_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            amt, acct = d(r["Amount"]), r["Account"].strip()
            if r["In profit"].strip().lower() != "yes":
                outside.append((r["Line"], acct, amt))
                continue
            section = SECTIONS.get(acct[:1])
            if section is None:
                ok = False
                print(f"'{r['Line']}' is marked In profit but {acct} is not a revenue or expense account.")
                continue
            by_section[section][acct] = by_section[section].get(acct, Decimal(0)) + abs(amt)
            if acct.startswith("60700"):
                gifts += abs(amt)
    totals = {}
    for section, accts in by_section.items():
        print(section)
        for acct, amt in sorted(accts.items()):
            print(f"  {acct:<40}{amt:>11,.2f}")
        totals[section] = sum(accts.values())
        print(f"  {'Total ' + section.lower():<40}{totals[section]:>11,.2f}")
    profit = totals["Revenue"] - totals["Cost of revenue"] - totals["Operating expenses"]
    print(f"{'Profit':<42}{profit:>11,.2f}")
    print("\nNot expenses (kept out of profit):")
    for line, acct, amt in outside:
        print(f"  {line:<40}{abs(amt):>11,.2f}  {acct}")
    if gifts:
        print(f"\nClient gifts booked: {gifts:,.2f}. The deduction is limited to $25 per person per year"
              " (IRS Publication 463); your tax preparer applies it.")

    business = commute = 0
    by_purpose = {}
    with open(miles_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            miles = int(r["Miles"])
            if r["Business"].strip().lower() == "yes":
                business += miles
                by_purpose[r["Purpose"]] = by_purpose.get(r["Purpose"], 0) + miles
            else:
                commute += miles
    print(f"\nMileage: {business} business miles, {commute} commuting miles left out")
    for purpose, miles in sorted(by_purpose.items(), key=lambda x: -x[1]):
        print(f"  {purpose:<40}{miles:>6}")
    print("\nAll checks pass." if ok else "\nSome checks failed; see above.")
    return ok


if __name__ == "__main__":
    a = sys.argv[1:] + [None] * 2
    sys.exit(0 if main(a[0] or "october-2026-month.csv", a[1] or "mileage-log-october-2026.csv") else 1)
