from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, t_type: str, amount: float, note: str, date_str: str = None):
        date_str = date_str or datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return False, "รูปแบบวันที่ไม่ถูกต้อง (YYYY-MM-DD)"
        
        if amount <= 0:
            return False, "จำนวนเงินต้องมากกว่า 0"

        self.transactions.append({"date": date_str, "type": t_type, "amount": amount, "note": note})
        return True, "บันทึกรายการสำเร็จ!"

    def get_summary(self, prefix: str):
        items = [t for t in self.transactions if t["date"].startswith(prefix)]
        inc = sum(t["amount"] for t in items if t["type"] == "income")
        exp = sum(t["amount"] for t in items if t["type"] == "expense")
        return {"income": inc, "expense": exp, "balance": inc - exp}

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n=== ระบบบันทึกรายรับ-รายจ่าย ===")
        print("1. บันทึกรายรับ (เงินเข้า)\n2. บันทึกรายจ่าย (เงินออก)\n3. สรุปยอดประจำวัน\n4. สรุปยอดประจำเดือน")
        
        choice = input("เลือกเมนู (1-4): ").strip()
        
        if choice in ["1", "2"]:
            t_type = "income" if choice == "1" else "expense"
            try:
                amt = float(input(f"กรอกจำนวนเงิน ({'รายรับ' if choice == '1' else 'รายจ่าย'}): "))
                note = input("รายละเอียดรายการ: ").strip()
                date_in = input("วันที่ (YYYY-MM-DD หรือเว้นว่างเพื่อใช้วันนี้): ").strip()
                _, msg = tracker.add_transaction(t_type, amt, note, date_in or None)
                print(f"-> {msg}")
            except ValueError:
                print("-> กรุณากรอกตัวเลขจำนวนเงินให้ถูกต้อง")
                
        elif choice in ["3", "4"]:
            fmt = "YYYY-MM-DD" if choice == "3" else "YYYY-MM"
            key = input(f"กรอก{'วันที่' if choice == '3' else 'เดือน'}ที่ต้องการสรุป ({fmt}): ").strip()
            res = tracker.get_summary(key)
            print(f"\n--- สรุปยอดประจำ {'วันที่' if choice == '3' else 'เดือน'} {key} ---")
            print(f"รายรับรวม  : {res['income']:,.2f} บาท\nรายจ่ายรวม : {res['expense']:,.2f} บาท\nคงเหลือสุทธิ: {res['balance']:,.2f} บาท")
            
        else:
            print("เมนูไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    main()
  