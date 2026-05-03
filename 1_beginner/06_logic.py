#  logical & comparison operators

# logical operators
# and --- both conditions are True
# or --- at least one condition is True
# not --- inverses any value

# AND orpetator
# hasStudied = True
# isReady = True

# if hasStudied and isReady:
#  print("can sit for the test") 

# OR operator
hasStudied = False
isReady = True

if hasStudied or isReady:
 print("Let's give him a trial") 

# NOT operator
# AND NOT Operation
isQualified = True
# badRecommendation = True
badRecommendation = False

if isQualified and not badRecommendation:
 print("Can be given the job") 

# OR NOT Operation
# hasCertification = True
hasCertification = False
badCredit = False

if hasCertification or not badCredit:
 print("You have one month to prove it") 
