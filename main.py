def bondPricing(interestRatePercent, principalValue, biannualCoupon, n_of_years):
  
  totalValue = 0
  #Coupon Net Present Value
  interest = interestRatePercent/100
  for i in range(n_of_years):
    year = i + 1
    value = (biannualCoupon * 2)/((1+interest) ** year)
    totalValue += value
  
  #Final Payment Value
  lastPayment = principalValue/((1+interest) ** n_of_years)
  totalValue += lastPayment

  totalreturn = (-(1 - (totalValue/principalValue))) * 100

  print('\n')
  print(f'The net present value of the bond is {totalValue}')
  print(f'The bond will return a total of {totalreturn}% at maturity')
  print(f'The annualized compounded return of the bond is {(-(1-((totalValue/principalValue) ** (1/n_of_years))))*100}% per year')
  return totalValue

principalValue = float(input('What is the principal value of the bond? '))
interestRatePercent = float(input('What is the interest rate of the the country? '))
biannualCoupon = float(input('How much does the borrower give out biannually as a coupon as dollars '))
years = int(input('How many years is the bond active for? '))

bondPricing(interestRatePercent, principalValue, biannualCoupon, years)
