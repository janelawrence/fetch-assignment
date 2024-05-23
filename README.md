# fetch-assignment


# ER Diagram

```mermaid
---
title: Receipts Scanned
---
erDiagram
    User ||--o{ Receipt : uploads
    Receipt ||--|{ Receipt-REWARD-ITEM : contains
    Receipt ||--|{RewardsStatus: has}
    BRAND }|..|{ Receipt-REWARD-ITEM : has

    User {
        int _id PK
        varchar(20) state
        varchar(50) signUpSource
        timestamp createdDate
        timestamp lastLogin
        str role 'CONSUMER'
        boolean active
    }

    Receipt {
        int _id PK
        int bonusPointsEarned
        str bonusPointsEarnedReason
        int pointsEarned
        int purchasedItemCount
        float totalSpent
        int userId
        RewardsStatus rewardsReceiptStatus
        timestamp createDate
        timestamp dateScanned
        timestamp finishedDate
        timestamp modifyDate
        timestamp pointsAwardedDate
        timestamp purchaseDate
    }

    RewardsStatus {
        enum FINISHED
        enum SUBMITTED
        enum REJECTED
        enum PENDING
        enum FLAGGED
    }

    Brand {
        int _id PK,
        str barcode
        str category
        str categoryCode
        str name
        boolean topBrand
        int cpg_id
        str cpg_ref
        str brandCode
    }

    ReceiptRewardItem {
        str barcode
        str brandCode
        int receiptId
        int partnerItemId
        int pointsPayerId
        str rewardsProductPartnerId
        str metabriteCampaignId
        str description
        float finalPrice
        float itemPrice
        boolean needsFetchReview
        boolean preventTargetGapPoints
        int quantityPurchased,
        int userFlaggedBarcode
        boolean userFlaggedNewItem
        float userFlaggedPrice
        int userFlaggedQuantity
        str needsFetchReviewReason
        str pointsNotAwardedReason
        str rewardsGroup
        str userFlaggedDescription
        str originalMetaBriteBarcode
        str originalMetaBriteDescription
        str competitorRewardsGroup
        float discountedItemPrice
        str originalReceiptItemText
        str itemNumber
        int originalMetaBriteQuantityPurchased
        float pointsEarned
        float targetPrice
        boolean competitiveProduct
        float originalFinalPrice
        float originalMetaBriteItemPrice
        boolean deleted
        float priceAfterCoupon
    }
```
