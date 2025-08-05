n, m = map(int,input().split())
min_total_budget = 0
min_package_budget = 1000
min_each_budget = 1000

for _ in range(m):
    package_budget, each_budget = map(int,input().split())

    if package_budget < min_package_budget: 
        min_package_budget = package_budget

    if each_budget < min_each_budget: 
        min_each_budget = each_budget

if (n % 6 != 0):
    min_total_budget += (min(min_package_budget, (min_each_budget * 6)) * (n // 6))
    n = (n % 6)
else:
    min_total_budget += (min((min_package_budget * (n // 6)), (min_each_budget * (n - (n % 6)))))
    n = (n % 6)

min_total_budget += min((min_package_budget), (min_each_budget * n))

print(min_total_budget)