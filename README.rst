probscales
----------

| Create matplotlib Scales from SciPy's continuous probability distributions.
| probscales enables rescaling of axes for plotting of data where one (or both) of x, y are probabilities.
| Log-scaling is commonly used in some disciplines, and is likely familiar from spreadsheet plots.
| Probability scaling has been used in psychology (AKA "probability paper") since the 1950's, and can be applied to any detection task.
| The Scale "xxx" scales the axis according to the Percent Point Function of the scipy.stats.xxx distribution.
| I.e. It maps x -> scipy.stats.xxx.ppf(x).
| The axis is scaled so that it is no longer linear for the interval [0, 1], but linear in the ppf.
| For a normal distribution, each standard deviation is a fixed distance apart.


E.g.

  >>> import matplotlib.pyplot as plt
  >>> import probscales
  >>> fig, ax = plt.subplots()
  >>> ax.plot(x_data, y_data)

Set the scale on the x-axis to a Normal distribution scale ("probability paper")

  >>> ax.set_xscale("norm")

Set the scale on the x-axis to a Normal distribution scale using percentages

  >>> ax.set_xscale("norm", percentage=True)

Set the scale on the x-axis to a Normal distribution scale with mean 1 and standard deviation 2

  >>> ax.set_xscale("norm", dist_kwargs={"loc" : 1, "scale" : 2})

Set the scale on the y-axis to a Student-t distribution scale with mean 1 and standard deviation 2

  >>> ax.set_yscale("t")

Set the scale on the y-axis to a beta distribution scale with parameters a=2, b=3

  >>> ax.set_xscale("beta", dist_kwargs={"a" : 2, "b" : 3})
  or
  >>> ax.set_xscale("beta", dist_args=(2, 3)})

The Scale named "probit" is an alias for the scale named "norm".

To turn an ROC (Receiver Operating Characteristic) curve into a DET (Detection Error Tradeoff) plot:

ROC:

  >>> p01 = np.linspace(0, 1, 11)
  >>> ax.plot(false_positive, true_positive, label="my great detector")
  >>> ax.plot(p01, p01, label="random monkeys")

DET:

  >>> ax.plot(false_positive, false_negative, label="my great detector")
  >>> ax.plot(p01, 1.0 - p01, label="random monkeys")
  >>> ax.set_xscale("norm")
  >>> ax.set_yscale("norm")

