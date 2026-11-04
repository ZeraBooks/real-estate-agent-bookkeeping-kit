"""Tie each closing's commission to the deposit the brokerage sent.

For every row in the closings file:
  your side    = sale price x total commission rate x your side's share
  split        = your side x brokerage split rate
  expected net = your side - split - transaction fee - other deductions
and the expected net must equal the deposit received. It then prints the
entry that books the closing gross: income for your side, the split and fees
as their own lines, the deposit to checking.

Usage: python3 check_closings.py closings-october-2026.csv
Python 3, standard library only.
"""
import csv
import sys
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def d(cell):
    cell = (cell or "").strip().replace(",", "")
    if cell.endswith("%"):
        return Decimal(cell[:-1]) / 100
    return Decimal(cell) if cell else Decimal("0")


def main(path):
    ok = True
    totals = {"side": Decimal(0), "split": Decimal(0), "fees": Decimal(0), "deposit": Decimal(0)}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            side = (d(r["Sale price"]) * d(r["Total commission rate"]) * d(r["Agent side share"])).quantize(CENT, ROUND_HALF_UP)
            split = (side * d(r["Brokerage split rate"])).quantize(CENT, ROUND_HALF_UP)
            fee, other, deposit = d(r["Transaction fee"]), d(r["Other deductions"]), d(r["Deposit received"])
            net = side - split - fee - other
            print(f"{r['Closing date']}  {r['Property']} ({r['Side']} side)")
            print(f"  Sale price {d(r['Sale price']):,.2f} x {r['Total commission rate']} x {r['Agent side share']} = your side {side:,.2f}")
            print(f"  Less split {split:,.2f}, transaction fee {fee:,.2f}, other {other:,.2f} = expected deposit {net:,.2f}")
            if net == deposit:
                print(f"  Deposit received {deposit:,.2f}: ties")
            else:
                ok = False
                print(f"  Deposit received {deposit:,.2f}: off by {deposit - net:+,.2f}. Get the commission statement and find the line.")
            entry = [("10100 Business checking", deposit, None), ("50100 Brokerage split", split, None),
                     ("50200 Transaction fees", fee, None)]
            if other:
                entry.append(("60300 E&O insurance" if "E&O" in r["Other deductions memo"] else "Other deduction: " + r["Other deductions memo"], other, None))
            entry.append(("40100 Gross commission income", None, side))
            dr = sum(e[1] for e in entry if e[1] is not None)
            cr = sum(e[2] for e in entry if e[2] is not None)
            print("  Entry:")
            for acct, debit, credit in entry:
                print(f"    {acct:<34}{(f'{debit:,.2f}' if debit is not None else ''):>11}{(f'{credit:,.2f}' if credit is not None else ''):>11}")
            print(f"    {'Totals':<34}{dr:>11,.2f}{cr:>11,.2f}{'' if dr == cr else '  DOES NOT BALANCE'}")
            if dr != cr:
                ok = False
            print()
            totals["side"] += side
            totals["split"] += split
            totals["fees"] += fee + other
            totals["deposit"] += deposit
    print(f"All closings: your side {totals['side']:,.2f}, split {totals['split']:,.2f}, "
          f"fees {totals['fees']:,.2f}, deposits {totals['deposit']:,.2f}")
    print("Every closing ties to its deposit." if ok else "Some closings don't tie; see above.")
    return ok


if __name__ == "__main__":
    sys.exit(0 if main(sys.argv[1] if len(sys.argv) > 1 else "closings-october-2026.csv") else 1)
