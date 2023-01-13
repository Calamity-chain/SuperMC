{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "453528da-6853-4b47-a598-8a7a39995393",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import glob\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2e438c7c-1510-42d0-8403-ec9f66d5752e",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "from_dict() got an unexpected keyword argument 'index'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_10159/2045947376.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mlocation_matrix\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfrom_dict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;34m'senior'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'junior'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mindex\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'dairy'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m'drinks'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m'fruit'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m'spices'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m'entry'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: from_dict() got an unexpected keyword argument 'index'"
     ]
    }
   ],
   "source": [
    "location_matrix = pd.DataFrame.from_dict({'senior': [0, 0, 0, 0, 0], 'junior': [0,0,0,0,0]}, index=['dairy','drinks','fruit','spices','entry'] )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dc622595-fd9e-41e3-921c-25119baa426b",
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
       "      <th>senior</th>\n",
       "      <th>junior</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>dairy</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>drinks</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fruit</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>spices</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>entry</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>checkout</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          senior  junior\n",
       "dairy          0       0\n",
       "drinks         0       0\n",
       "fruit          0       0\n",
       "spices         0       0\n",
       "entry          0       0\n",
       "checkout       0       0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "location_matrix = pd.DataFrame(columns=['senior', 'junior'], index=['dairy','drinks','fruit','spices','entry','checkout']).fillna(value=0)\n",
    "location_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2597073d-e4c6-4a54-b5dc-6e76d205d941",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b95d4b18-4e5d-4ead-b7be-21e2eaaccfa7",
   "metadata": {},
   "outputs": [],
   "source": [
    "class SM:\n",
    "    def __init__(self, closing=900):\n",
    "        self.closing         = closing # 900minutes(15h), 900 steps.\n",
    "\n",
    "        #this keeps number of senior and juniors at sections (time i)\n",
    "        self.location_matrix   = pd.DataFrame(columns=['senior', 'junior'], index=['dairy','drinks','fruit','spices','entry']).fillna(value=0)\n",
    "        #this keeps new number for locations (time i+1)\n",
    "        self.temp_location     = location_matrix.copy\n",
    "        #Before temp location is overwritten, it written in this data frame every turn\n",
    "        self.customer_record   = location_matrix.copy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5f644de0-cea6-4609-9675-c6aa9168c4d1",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'self' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_10159/3200100852.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlocation_matrix\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'self' is not defined"
     ]
    }
   ],
   "source": [
    "self.location_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc1a1388-97ac-492e-8916-5e861cfc8093",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
