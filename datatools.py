import numpy as np




def climatology(dates, var):
	""" date -- list of datetime objects
		var -- variable to compute climatology on
	"""
	jan_ind = 0; feb_ind = 0; mar_ind = 0; apr_ind = 0; may_ind = 0; jun_ind = 0 
	jul_ind = 0; aug_ind = 0; sep_ind = 0; oct_ind = 0; nov_ind = 0; dec_ind = 0

	jan = 0; feb = 0; mar = 0; apr = 0; may = 0; jun = 0
	jul = 0; aug = 0; sep = 0; oct = 0; nov = 0; dec = 0
	for i in range(len(dates)):
		if np.isfinite(var[i]) == True: 
			if dates[i].month == 1:
				jan_ind += 1
				jan += var[i]
			if dates[i].month == 2:
				feb_ind += 1
				feb += var[i]
			if dates[i].month == 3:
				mar_ind += 1
				mar += var[i]
			if dates[i].month == 4:
				apr_ind += 1
				apr += var[i]
			if dates[i].month == 5:
				may_ind += 1
				may += var[i]
			if dates[i].month == 6:
				jun_ind += 1
				jun += var[i]
			if dates[i].month == 7:
				jul_ind += 1
				jul += var[i]
			if dates[i].month == 8:
				aug_ind += 1
				aug += var[i]
			if dates[i].month == 9:
				sep_ind += 1
				sep += var[i]
			if dates[i].month == 10:
				oct_ind += 1
				oct += var[i]
			if dates[i].month == 11:
				nov_ind += 1
				nov += var[i]
			if dates[i].month == 12:
				dec_ind += 1
				dec += var[i]
	return np.array([jan/jan_ind, feb/feb_ind, mar/mar_ind, apr/apr_ind, may/may_ind, jun/jun_ind, jul/jul_ind, aug/aug_ind, sep/sep_ind, oct/oct_ind, nov/nov_ind, dec/dec_ind])
