import matplotlib.pyplot as plt
import pandas as pd

wp = pd.read_csv('/Users/garrettwankel/sqlite/wp.csv', index_col=0)
print(wp)

hp = wp.iloc[0:8]
lp = wp.iloc[8:31]

gdp1 = hp['GDP (US$mil)']
la1 = hp['land area (sq mi)']
pop1 = hp['population (mil)']

gdp2 = lp['GDP (US$mil)']
la2 = lp['land area (sq mi)']
pop2 = lp['population (mil)']


plt.subplot(1, 2, 1)
plt.scatter(pop2, gdp2)
plt.xlabel('Population (mil)')
plt.ylabel('GDP (US $mil)')
plt.title('Population vs. GDP')
plt.ticklabel_format(useOffset=False, style='plain')

plt.subplot(1, 2, 2)
plt.scatter(pop1, gdp1)
plt.xlabel('Population (mil)')
plt.ylabel('GDP (US $mil)')
plt.title('Population vs. GDP')
plt.ticklabel_format(useOffset=False, style='plain')
plt.show()
