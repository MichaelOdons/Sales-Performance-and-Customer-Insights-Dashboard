{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "61d68fbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\hp\\\\Documents'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.getcwd()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ffcba01f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "os.chdir(r\"C:\\Users\\hp\\Documents\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "6c6b8399",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"cleaned_data_xlsx.csv\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "4197d653",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Row ID</th>\n",
       "      <th>Order ID</th>\n",
       "      <th>Order Date</th>\n",
       "      <th>Ship Date</th>\n",
       "      <th>Ship Mode</th>\n",
       "      <th>Customer ID</th>\n",
       "      <th>Customer Name</th>\n",
       "      <th>Segment</th>\n",
       "      <th>Country</th>\n",
       "      <th>City</th>\n",
       "      <th>...</th>\n",
       "      <th>Postal Code</th>\n",
       "      <th>Region</th>\n",
       "      <th>Product ID</th>\n",
       "      <th>Category</th>\n",
       "      <th>Sub-Category</th>\n",
       "      <th>Product Name</th>\n",
       "      <th>Sales</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Discount</th>\n",
       "      <th>Profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>CA-2016-152156</td>\n",
       "      <td>11/8/2016</td>\n",
       "      <td>11/11/2016</td>\n",
       "      <td>Second Class</td>\n",
       "      <td>CG-12520</td>\n",
       "      <td>Claire Gute</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Henderson</td>\n",
       "      <td>...</td>\n",
       "      <td>42420</td>\n",
       "      <td>South</td>\n",
       "      <td>FUR-BO-10001798</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Bookcases</td>\n",
       "      <td>Bush Somerset Collection Bookcase</td>\n",
       "      <td>261.96</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>41.91</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>CA-2016-152156</td>\n",
       "      <td>11/8/2016</td>\n",
       "      <td>11/11/2016</td>\n",
       "      <td>Second Class</td>\n",
       "      <td>CG-12520</td>\n",
       "      <td>Claire Gute</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Henderson</td>\n",
       "      <td>...</td>\n",
       "      <td>42420</td>\n",
       "      <td>South</td>\n",
       "      <td>FUR-CH-10000454</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Chairs</td>\n",
       "      <td>Hon Deluxe Fabric Upholstered Stacking Chairs,...</td>\n",
       "      <td>731.94</td>\n",
       "      <td>3</td>\n",
       "      <td>0.00</td>\n",
       "      <td>219.58</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>CA-2016-138688</td>\n",
       "      <td>6/12/2016</td>\n",
       "      <td>6/16/2016</td>\n",
       "      <td>Second Class</td>\n",
       "      <td>DV-13045</td>\n",
       "      <td>Darrin Van Huff</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>United States</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>...</td>\n",
       "      <td>90036</td>\n",
       "      <td>West</td>\n",
       "      <td>OFF-LA-10000240</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Labels</td>\n",
       "      <td>Self-Adhesive Address Labels for Typewriters b...</td>\n",
       "      <td>14.62</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>6.87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>US-2015-108966</td>\n",
       "      <td>10/11/2015</td>\n",
       "      <td>10/18/2015</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>SO-20335</td>\n",
       "      <td>Sean O'Donnell</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Fort Lauderdale</td>\n",
       "      <td>...</td>\n",
       "      <td>33311</td>\n",
       "      <td>South</td>\n",
       "      <td>FUR-TA-10000577</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Tables</td>\n",
       "      <td>Bretford CR4500 Series Slim Rectangular Table</td>\n",
       "      <td>957.58</td>\n",
       "      <td>5</td>\n",
       "      <td>0.45</td>\n",
       "      <td>-383.03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>US-2015-108966</td>\n",
       "      <td>10/11/2015</td>\n",
       "      <td>10/18/2015</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>SO-20335</td>\n",
       "      <td>Sean O'Donnell</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Fort Lauderdale</td>\n",
       "      <td>...</td>\n",
       "      <td>33311</td>\n",
       "      <td>South</td>\n",
       "      <td>OFF-ST-10000760</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Storage</td>\n",
       "      <td>Eldon Fold 'N Roll Cart System</td>\n",
       "      <td>22.37</td>\n",
       "      <td>2</td>\n",
       "      <td>0.20</td>\n",
       "      <td>2.52</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Row ID        Order ID  Order Date   Ship Date       Ship Mode Customer ID  \\\n",
       "0       1  CA-2016-152156   11/8/2016  11/11/2016    Second Class    CG-12520   \n",
       "1       2  CA-2016-152156   11/8/2016  11/11/2016    Second Class    CG-12520   \n",
       "2       3  CA-2016-138688   6/12/2016   6/16/2016    Second Class    DV-13045   \n",
       "3       4  US-2015-108966  10/11/2015  10/18/2015  Standard Class    SO-20335   \n",
       "4       5  US-2015-108966  10/11/2015  10/18/2015  Standard Class    SO-20335   \n",
       "\n",
       "     Customer Name    Segment        Country             City  ...  \\\n",
       "0      Claire Gute   Consumer  United States        Henderson  ...   \n",
       "1      Claire Gute   Consumer  United States        Henderson  ...   \n",
       "2  Darrin Van Huff  Corporate  United States      Los Angeles  ...   \n",
       "3   Sean O'Donnell   Consumer  United States  Fort Lauderdale  ...   \n",
       "4   Sean O'Donnell   Consumer  United States  Fort Lauderdale  ...   \n",
       "\n",
       "  Postal Code  Region       Product ID         Category Sub-Category  \\\n",
       "0       42420   South  FUR-BO-10001798        Furniture    Bookcases   \n",
       "1       42420   South  FUR-CH-10000454        Furniture       Chairs   \n",
       "2       90036    West  OFF-LA-10000240  Office Supplies       Labels   \n",
       "3       33311   South  FUR-TA-10000577        Furniture       Tables   \n",
       "4       33311   South  OFF-ST-10000760  Office Supplies      Storage   \n",
       "\n",
       "                                        Product Name   Sales  Quantity  \\\n",
       "0                  Bush Somerset Collection Bookcase  261.96         2   \n",
       "1  Hon Deluxe Fabric Upholstered Stacking Chairs,...  731.94         3   \n",
       "2  Self-Adhesive Address Labels for Typewriters b...   14.62         2   \n",
       "3      Bretford CR4500 Series Slim Rectangular Table  957.58         5   \n",
       "4                     Eldon Fold 'N Roll Cart System   22.37         2   \n",
       "\n",
       "   Discount  Profit  \n",
       "0      0.00   41.91  \n",
       "1      0.00  219.58  \n",
       "2      0.00    6.87  \n",
       "3      0.45 -383.03  \n",
       "4      0.20    2.52  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "61600741",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 9994 entries, 0 to 9993\n",
      "Data columns (total 21 columns):\n",
      " #   Column         Non-Null Count  Dtype  \n",
      "---  ------         --------------  -----  \n",
      " 0   Row ID         9994 non-null   int64  \n",
      " 1   Order ID       9994 non-null   object \n",
      " 2   Order Date     9994 non-null   object \n",
      " 3   Ship Date      9994 non-null   object \n",
      " 4   Ship Mode      9994 non-null   object \n",
      " 5   Customer ID    9994 non-null   object \n",
      " 6   Customer Name  9994 non-null   object \n",
      " 7   Segment        9994 non-null   object \n",
      " 8   Country        9994 non-null   object \n",
      " 9   City           9994 non-null   object \n",
      " 10  State          9994 non-null   object \n",
      " 11  Postal Code    9994 non-null   int64  \n",
      " 12  Region         9994 non-null   object \n",
      " 13  Product ID     9994 non-null   object \n",
      " 14  Category       9994 non-null   object \n",
      " 15  Sub-Category   9994 non-null   object \n",
      " 16  Product Name   9994 non-null   object \n",
      " 17  Sales          9994 non-null   float64\n",
      " 18  Quantity       9994 non-null   int64  \n",
      " 19  Discount       9994 non-null   float64\n",
      " 20  Profit         9994 non-null   float64\n",
      "dtypes: float64(3), int64(3), object(15)\n",
      "memory usage: 1.6+ MB\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Row ID</th>\n",
       "      <th>Postal Code</th>\n",
       "      <th>Sales</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Discount</th>\n",
       "      <th>Profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>9994.000000</td>\n",
       "      <td>9994.000000</td>\n",
       "      <td>9994.000000</td>\n",
       "      <td>9994.000000</td>\n",
       "      <td>9994.000000</td>\n",
       "      <td>9994.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4997.500000</td>\n",
       "      <td>55190.379428</td>\n",
       "      <td>229.858022</td>\n",
       "      <td>3.789574</td>\n",
       "      <td>0.156203</td>\n",
       "      <td>28.656973</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2885.163629</td>\n",
       "      <td>32063.693350</td>\n",
       "      <td>623.245131</td>\n",
       "      <td>2.225110</td>\n",
       "      <td>0.206452</td>\n",
       "      <td>234.260203</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1040.000000</td>\n",
       "      <td>0.440000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-6599.980000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2499.250000</td>\n",
       "      <td>23223.000000</td>\n",
       "      <td>17.280000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.730000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4997.500000</td>\n",
       "      <td>56430.500000</td>\n",
       "      <td>54.490000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.200000</td>\n",
       "      <td>8.665000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7495.750000</td>\n",
       "      <td>90008.000000</td>\n",
       "      <td>209.940000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>0.200000</td>\n",
       "      <td>29.360000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9994.000000</td>\n",
       "      <td>99301.000000</td>\n",
       "      <td>22638.480000</td>\n",
       "      <td>14.000000</td>\n",
       "      <td>0.800000</td>\n",
       "      <td>8399.980000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Row ID   Postal Code         Sales     Quantity     Discount  \\\n",
       "count  9994.000000   9994.000000   9994.000000  9994.000000  9994.000000   \n",
       "mean   4997.500000  55190.379428    229.858022     3.789574     0.156203   \n",
       "std    2885.163629  32063.693350    623.245131     2.225110     0.206452   \n",
       "min       1.000000   1040.000000      0.440000     1.000000     0.000000   \n",
       "25%    2499.250000  23223.000000     17.280000     2.000000     0.000000   \n",
       "50%    4997.500000  56430.500000     54.490000     3.000000     0.200000   \n",
       "75%    7495.750000  90008.000000    209.940000     5.000000     0.200000   \n",
       "max    9994.000000  99301.000000  22638.480000    14.000000     0.800000   \n",
       "\n",
       "            Profit  \n",
       "count  9994.000000  \n",
       "mean     28.656973  \n",
       "std     234.260203  \n",
       "min   -6599.980000  \n",
       "25%       1.730000  \n",
       "50%       8.665000  \n",
       "75%      29.360000  \n",
       "max    8399.980000  "
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.info()\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "8271a2d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.drop_duplicates()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "e49650d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.dropna()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "0ea46ec6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Order Date'] = pd.to_datetime(df['Order Date'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "ba7437f0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2297201.07"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Sales'].sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "ad42909a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "286397.79000000004"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Profit'].sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "28f81592",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Region\n",
       "West       725457.93\n",
       "East       678781.36\n",
       "Central    501239.88\n",
       "South      391721.90\n",
       "Name: Sales, dtype: float64"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Region')['Sales'].sum().sort_values(ascending=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "8ac47bb3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Order Date\n",
       "2014-01     14236.90\n",
       "2014-02      4519.92\n",
       "2014-03     55691.04\n",
       "2014-04     28295.35\n",
       "2014-05     23648.28\n",
       "2014-06     34595.14\n",
       "2014-07     33946.37\n",
       "2014-08     27909.47\n",
       "2014-09     81777.34\n",
       "2014-10     31453.37\n",
       "2014-11     78628.74\n",
       "2014-12     69545.64\n",
       "2015-01     18174.08\n",
       "2015-02     11951.40\n",
       "2015-03     38726.26\n",
       "2015-04     34195.25\n",
       "2015-05     30131.72\n",
       "2015-06     24797.31\n",
       "2015-07     28765.32\n",
       "2015-08     36898.32\n",
       "2015-09     64595.87\n",
       "2015-10     31404.90\n",
       "2015-11     75972.51\n",
       "2015-12     74919.52\n",
       "2016-01     18542.52\n",
       "2016-02     22978.82\n",
       "2016-03     51715.86\n",
       "2016-04     38750.04\n",
       "2016-05     56987.75\n",
       "2016-06     40344.54\n",
       "2016-07     39261.99\n",
       "2016-08     31115.35\n",
       "2016-09     73410.09\n",
       "2016-10     59687.80\n",
       "2016-11     79412.03\n",
       "2016-12     96999.07\n",
       "2017-01     43971.37\n",
       "2017-02     20301.12\n",
       "2017-03     58872.35\n",
       "2017-04     36521.52\n",
       "2017-05     44261.08\n",
       "2017-06     52981.73\n",
       "2017-07     45264.43\n",
       "2017-08     63120.85\n",
       "2017-09     87866.66\n",
       "2017-10     77776.96\n",
       "2017-11    118447.81\n",
       "2017-12     83829.31\n",
       "Freq: M, Name: Sales, dtype: float64"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Order Date'] = df['Order Date'].dt.to_period('M')\n",
    "\n",
    "df.groupby('Order Date')['Sales'].sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "7284667a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "7a0c2e2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.dropna(subset=['Sales'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "f24522be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Row ID               int64\n",
       "Order ID            object\n",
       "Order Date       period[M]\n",
       "Ship Date           object\n",
       "Ship Mode           object\n",
       "Customer ID         object\n",
       "Customer Name       object\n",
       "Segment             object\n",
       "Country             object\n",
       "City                object\n",
       "State               object\n",
       "Postal Code          int64\n",
       "Region              object\n",
       "Product ID          object\n",
       "Category            object\n",
       "Sub-Category        object\n",
       "Product Name        object\n",
       "Sales              float64\n",
       "Quantity             int64\n",
       "Discount           float64\n",
       "Profit             float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "55034e00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',\n",
      "       'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State',\n",
      "       'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category',\n",
      "       'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(df.columns)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "41dc0c46",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.columns = df.columns.str.strip()  # removes spaces\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "00fe1711",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Row ID               int64\n",
      "Order ID            object\n",
      "Order Date       period[M]\n",
      "Ship Date           object\n",
      "Ship Mode           object\n",
      "Customer ID         object\n",
      "Customer Name       object\n",
      "Segment             object\n",
      "Country             object\n",
      "City                object\n",
      "State               object\n",
      "Postal Code          int64\n",
      "Region              object\n",
      "Product ID          object\n",
      "Category            object\n",
      "Sub-Category        object\n",
      "Product Name        object\n",
      "Sales              float64\n",
      "Quantity             int64\n",
      "Discount           float64\n",
      "Profit             float64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(df.dtypes)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "edae020e",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.dropna(subset=['Sales'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "abfb147c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Region\n",
      "Central    501239.88\n",
      "East       678781.36\n",
      "South      391721.90\n",
      "West       725457.93\n",
      "Name: Sales, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "grouped = df.groupby('Region')['Sales'].sum()\n",
    "print(grouped)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "1ae500ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['row_id', 'order_id', 'order_date', 'ship_date', 'ship_mode',\n",
      "       'customer_id', 'customer_name', 'segment', 'country', 'city', 'state',\n",
      "       'postal_code', 'region', 'product_id', 'category', 'sub-category',\n",
      "       'product_name', 'sales', 'quantity', 'discount', 'profit'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "# Remove leading/trailing spaces, lowercase, replace spaces with underscore\n",
    "df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')\n",
    "print(df.columns)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "24d0ae95",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remove $ or , and convert to numeric\n",
    "df['sales'] = df['sales'].astype(str).str.replace(',', '').str.replace('$','')\n",
    "df['sales'] = pd.to_numeric(df['sales'], errors='coerce')\n",
    "\n",
    "# Drop rows with missing sales\n",
    "df = df.dropna(subset=['sales'])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "f475d62a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "region\n",
      "Central    501239.88\n",
      "East       678781.36\n",
      "South      391721.90\n",
      "West       725457.93\n",
      "Name: sales, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "grouped = df.groupby('region')['sales'].sum()\n",
    "print(grouped)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "058e6053",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['South' 'West' 'Central' 'East']\n"
     ]
    }
   ],
   "source": [
    "print(df['region'].unique())\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "7cdc7056",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlYAAAHpCAYAAABA0XIiAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABSzklEQVR4nO3df1yV9f3/8eeJH0dEOWIIeIxEzZyE9kObohWYipY/aq3ZhpIs42P5gxi6lnOb5ifRnGJNy21+mjp/pG1Ga7kINEVJUfxBiZo108AEscKDGgHB9f3Dr9d2REnrwiPyuN9u53bzXNfrnOt1rpP47H29rzc2wzAMAQAA4Hu7ztMNAAAAXCsIVgAAABYhWAEAAFiEYAUAAGARghUAAIBFCFYAAAAWIVgBAABYhGAFAABgEYIVAACARQhWACyzfft2/ehHP9KNN94ou92ukJAQRUVFadKkSd/p/aZPny6bzWZxl/VLSEhQixYtGvw4MTExstls5qNZs2aKiIjQc889p6qqqgY99pEjR2Sz2bR06dIGPQ7QFBGsAFhi3bp16tOnj8rLyzVnzhxlZmbqxRdfVN++fbVmzRpPt3dV6tixo7Zt26Zt27bpb3/7mzp37qzf/va3mjBhQoMet23bttq2bZuGDBnSoMcBmiIbvysQgBWio6P12Wef6cMPP5S3t7fbvtraWl133eX/f9z06dP17LPP6kr+mEpISNDf//53nT59ukGPExMTo88//1wFBQXmtm+++UYRERH69NNP5XK51KxZswbtAYD1GLECYIkvvvhCQUFBdUKVpDqhas2aNYqNjVXbtm3l5+enrl276plnntGZM2cu6Vhr1qxRVFSU/P391aJFCw0aNEh79uxxq/nkk0/005/+VE6n07ws2b9/f+Xn51/SMfbt26f+/fvL399fbdq00YQJE/TVV1+Z+/v3768f/OAHdUKfYRi66aabvtNokLe3t2677TZVVVXp5MmTbu/58ssv67bbbpOfn58CAwP18MMP65NPPqlz7NTUVLVv317NmjVTz549lZWVpZiYGMXExJh1F7sUmJOTo/79+6tly5Zq3ry5+vTpo3Xr1rnVLF26VDabTRs3btSTTz6poKAgXX/99XrooYd07Nixy/7MwLWGYAXAElFRUdq+fbuSkpK0fft2VVdXX7T2448/1v33369XXnlFGRkZSk5O1muvvaZhw4Z963FSU1P1s5/9TBEREXrttde0fPlynTp1Snfffbf2799v1t1///3atWuX5syZo6ysLC1atEi33367W2C5mOrqat1///3q37+/3njjDU2YMEF/+tOf9Mgjj5g1Tz31lA4ePKgNGza4vfbtt9/WoUOHNH78+G89zoUcPnxYrVq1Ups2bcxtY8eOVXJysgYMGKA33nhDL7/8svbt26c+ffro+PHjZt3UqVM1depUDR48WP/4xz/0xBNP6PHHH9dHH330rcfNzs7WvffeK5fLpVdeeUWvvvqqWrZsqWHDhl3wUu7jjz8uHx8frVq1SnPmzNGmTZs0atSo7/SZgWuKAQAW+Pzzz4277rrLkGRIMnx8fIw+ffoYs2bNMk6dOnXR19XW1hrV1dVGdna2Icl4//33zX3Tpk0z/vvHVGFhoeHt7W1MnDjR7T1OnTplhIaGGiNGjDB7kWS88MILl/05Ro8ebUgyXnzxRbftM2fONCQZOTk5hmEYRk1NjdGxY0fjgQcecKu77777jE6dOhm1tbX1Hic6Otq45ZZbjOrqaqO6utooLi42fve73xmSjD/+8Y9m3bZt2wxJxrx589xeX1RUZPj5+RlPP/20YRiG8eWXXxp2u9145JFH3OrOvT46OtrcdvjwYUOSsWTJEnNb7969jeDgYLfv6ptvvjEiIyONG264wfw8S5YsMSQZ48aNczvOnDlzDElGcXFxvZ8buNYxYgXAEtdff722bNmivLw8zZ49Ww888IA++ugjTZkyRd26ddPnn39u1n7yySeKi4tTaGiovLy85OPjo+joaEnSgQMHLnqMd955R998840effRRffPNN+ajWbNmio6O1qZNmyRJrVu3VqdOnfT73/9eaWlp2rNnj2pray/r84wcOdLteVxcnCRp48aNks5e3pwwYYLeeustFRYWSpIOHTqkjIwMjRs37pLuZty3b598fHzk4+Ojtm3basaMGZoyZYrGjh1r1rz11luy2WwaNWqU22cODQ3Vrbfean7m3NxcVVZWasSIEW7H6N27t8LDw+vt48yZM9q+fbsefvhhtzsivby8FB8fr6NHj+rgwYNurxk+fLjb8+7du0uSPv3002/93MC1jGAFwFI9e/bUr371K/3tb3/TsWPH9Itf/EJHjhzRnDlzJEmnT5/W3Xffre3bt+u5557Tpk2blJeXp9dff12SVFFRcdH3PnfZ68477zQDybnHmjVrzPBms9m0YcMGDRo0SHPmzNEdd9yhNm3aKCkpSadOnfrWz+Dt7a3rr7/ebVtoaKiks3PJznnsscfk5+enP/7xj5Kkl156SX5+fnrssccu6Vx16tRJeXl52rFjh/72t7/p1ltv1axZs7R69Wq3z2wYhkJCQup85tzcXPMzn+srJCSkznEutO2/lZWVyTAMtW3bts4+p9NZ53NLqnN+7Ha7pPq/P6ApqDvLFAAs4uPjo2nTpmn+/Pnm3W/vvvuujh07pk2bNpmjVJIuae5TUFCQJOnvf/+72rdvX29t+/bt9corr0iSPvroI7322muaPn26qqqqzCB0Md98842++OILt/BQUlIiyT1QOBwOjR49Wv/3f/+nyZMna8mSJYqLi1OrVq2+9bNIMieYS2fDYr9+/XTLLbcoOTlZQ4cOVYsWLRQUFCSbzaYtW7aY4eW/ndt2rq//nnP1373XN2oVGBio6667TsXFxXX2nZuQfu7cA6gfI1YALHGhf5Sl/1zaOzfyce4S2fkh4U9/+tO3HmPQoEHy9vbWoUOH1LNnzws+LuTmm2/Wb37zG3Xr1k27d+++pM+zcuVKt+erVq2SJLe76yQpKSlJn3/+uR5++GGdPHnye61Bdf3112v27Nk6fvy4FixYIEkaOnSoDMPQZ599dsHP261bN0lSr169ZLfb60w0z83N/dbLc/7+/urVq5def/11txGn2tparVixQjfccINuvvnm7/y5gKaEESsAlhg0aJBuuOEGDRs2TD/4wQ9UW1ur/Px8zZs3Ty1atNBTTz0lSerTp48CAwP1xBNPaNq0afLx8dHKlSv1/vvvf+sxwsPDNWPGDE2dOlWffPKJBg8erMDAQB0/flw7duyQv7+/nn32WX3wwQeaMGGCfvKTn6hz587y9fXVu+++qw8++EDPPPPMtx7H19dX8+bN0+nTp3XnnXdq69ateu6553Tffffprrvucqu9+eabNXjwYL399tu66667dOutt363E/j/Pfroo0pLS9PcuXM1fvx49e3bV//zP/+jn//859q5c6fuuece+fv7q7i4WDk5OerWrZuefPJJtW7dWikpKZo1a5YCAwP1ox/9SEePHtWzzz6rtm3bfus6YrNmzdLAgQPVr18/TZ48Wb6+vnr55ZdVUFCgV1999Yqv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735+s8K1JSoqSj/5yU+UkpJiLvjcsWNH5eXl6cEHH9Rnn33m6RavKkxeR4PYuHGjp1vAFfb0009r48aNevnll/Xoo4/qpZde0meffaY//elPmj17tqfbg4VuvfVWt+fV1dXKz89XQUGBRo8e7aGu0FD27t2rVatW1dnepk2bC/5PVFNHsEKD6NChAwsINjH//Oc/9de//lUxMTF67LHHdPfdd+umm25S+/bttXLlSo0cOdLTLcIiF1sy5dzSKri2tGrVSsXFxXVuRtqzZ495hyD+gzlWaBAdOnTQiRMn6mw/t4Agrj3//d0GBAToyy+/lHR2GYbNmzd7sjVcIaNGjdJf/vIXT7cBi8XFxelXv/qVSkpKZLPZVFtbq/fee0+TJ08216vDfxCs0CBYQLDp6dixo/k7ICMiIvTaa69JOjuS1apVK881hitm27Zt/P2+hvz73/+WdPZmpPbt26tdu3Y6ffq0IiIidM8996hPnz76zW9+4+Eurz5cCoSlWECw6fr5z3+u999/X9HR0ZoyZYqGDBmiBQsW6JtvvtG8efM83R4s9NBDD7k9NwxDxcXF2rlzp3772996qCtY7eabb1a7du3Ur18/9e/fXzNmzNDu3btVW1ur22+/nfXKLoK7AmEpFhDEOYWFhdq5c6c6depUZ7IzGref//znbs+vu+46tWnTRvfee69iY2M91BWstmXLFmVnZ2vTpk3atm2bvv76a914442699571a9fP/Xr1485VhdAsEKDYAHBpuP+++/Xq6++KofDIensZYPx48ebl/+++OIL3X333dq/f78HuwTwfVRXV2vbtm3atGmTNm3apNzcXFVWVuqmm27SwYMHPd3eVYVgBeB78fLyUnFxsYKDgyWdnbien5+vjh07SpKOHz8up9PJOlbXoF27dunAgQOy2WyKiIjQ7bff7umW0MAqKiqUk5Ojd955R4sXL9bp06f5u30e5lihQZw5c0azZ8/Whg0bVFpaqtraWrf9n3zyiYc6g9XO/38z/l/t2ldaWqqf/vSn2rRpk1q1aiXDMORyudSvXz+tXr1abdq08XSLsMjXX3+trVu3auPGjdq0aZPy8vLUoUMHRUdHa9GiRYqOjvZ0i1cdghUaxOOPP67s7GzFx8erbdu2F7xDEEDjNHHiRJWXl2vfvn3q2rWrJGn//v0aPXq0kpKS9Oqrr3q4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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "grouped.plot(kind='bar')\n",
    "plt.title(\"Sales by Region\")\n",
    "plt.ylabel(\"Total Sales\")\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "1b8bc043",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(\"sales_data_final.csv\", index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b358bc3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
