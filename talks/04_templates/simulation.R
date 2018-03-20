rm(list=ls())
library(deSolve)

# ----------------------
# import odes
# ----------------------
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
source("./results/lorenz.R")

# ----------------------
# MBT (simulation)
# ----------------------

# desolve simulation
times <- seq(0, 20, by=0.01)

# ODE integration
X <- ode(y=x0, times=times, func=f_dxdt, parms=p)

# Solution Matrix
s = f_z(times, X, p)

# png(filename="./results/lorenz_desolve.png", width=1200, height=1200)
# plot results
par(mfrow = c(2, 2))
plot(s[, 'time'], s[, 'x'], type="l", ylim=c(-40, 80),
     main="desolve",
     xlab='time',
     ylab='value')
lines(s[, 'time'], s[, 'y'], type="l")
lines(s[, 'time'], s[, 'z'], type="l")

# plot results
plot(s[, 'x'], s[, 'y'], type="l",
     main="desolve (y ~ x)",
     xlab='value',
     ylab='value')
plot(s[, 'x'], s[, 'z'], type="l",
     main="desolve (z ~ x)",
     xlab='value',
     ylab='value')
plot(s[, 'y'], s[, 'z'], type="l",
     main="desolve (z ~ y)",
     xlab='value',
     ylab='value')
# dev.off()
par(mfrow = c(1, 1))
