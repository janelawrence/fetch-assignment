# fetch-assignment


# ER Diagram

```mermaid
---
title: Receipts Scanned
---
erDiagram
    User ||--o{ Receipt : uploads
    Receipt ||--|{ ReceiptRewardItem : contains
    Receipt ||--|{ RewardsStatus: has
    Brand }|..|{ ReceiptRewardItem : has

    User {
        string(255) _id PK
        varchar(20) state
        varchar(50) signUpSource
        timestamp createdDate
        timestamp lastLogin
        UserRole role
        boolean active
    }

    Receipt {
        string(255) _id PK
        int bonusPointsEarned
        str bonusPointsEarnedReason
        int pointsEarned
        int purchasedItemCount
        float totalSpent
        string(255)  userId
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

    UserRole {
        enum CONSUMER
        enum FETCH-STAFF
    }

    Brand {
        string(255) _id PK
        str barcode
        str category
        str categoryCode
        str name
        boolean topBrand
        string(255) cpg.id.oid
        text cpg.ref
        str brandCode
    }

    ReceiptRewardItem {
        String(255) barcode
        String(255) brandCode
        String(255) receiptId
        String(255) partnerItemId
        String(255) pointsPayerId
        String(255) rewardsProductPartnerId
        String(255) metabriteCampaignId
        str description
        float finalPrice
        float itemPrice
        boolean needsFetchReview
        boolean preventTargetGapPoints
        int quantityPurchased
        String(255) userFlaggedBarcode
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
