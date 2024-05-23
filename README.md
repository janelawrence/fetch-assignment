# fetch-assignment


# ER Diagram

```mermaid
---
title: Receipts Scanned
---
erDiagram
    USER ||--o{ RECEIPT : uploads
    RECEIPT ||--|{ RECEIPT-REWARD-ITEM : contains
    BRAND }|..|{ RECEIPT-REWARD-ITEM : contains
```
