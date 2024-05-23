# fetch-assignment


# ER Diagram


---
title: Receipts Scanned
---
erDiagram
    USER ||--o{ RECEIPT : uploads
    RECEIPT ||--|{ RECEIPT-REWARD-ITEM : contains
    BRAND }|..|{ RECEIPT-REWARD-ITEM : contains
