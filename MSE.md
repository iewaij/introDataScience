$$
\begin{equation}
\begin{split}
MSE
 &= \mathrm{E}[(w - \hat{w})^2]\\
 &= \mathrm{E}\big[ [w - \mathrm{E}(\hat{w}) + \mathrm{E}(\hat{w}) - \hat{w}]^2 \big]\\
 &= \mathrm{E}\big[ [w - \mathrm{E}(\hat{w})]^2 + [\hat{w}-\mathrm{E}(\hat{w})]^2 + 2[w - \mathrm{E}(\hat{w})][\mathrm{E}(\hat{w}) - \hat{w}] \big] \\
 &= \mathrm{E}\big[ [w - \mathrm{E}(\hat{w})]^2\big] + \mathrm{E}\big[[\hat{w}-\mathrm{E}(\hat{w})]^2\big] + \mathrm{E}\big[2[w - \mathrm{E}(\hat{w})][\mathrm{E}(\hat{w}) - \hat{w}] \big] \\
\end{split}
\end{equation}
$$

由于 $\mathrm{E}\big[[\mathrm{E}(\hat{w}) - \hat{w}] \big]=0$，因此

$$
\begin{equation}
\begin{split}
MSE
 &= \mathrm{E}[(w - \hat{w})^2]\\
 &= \mathrm{E}\big[ [w - \mathrm{E}(\hat{w})]^2\big] + \mathrm{E}\big[[\hat{w}-\mathrm{E}(\hat{w})]^2\big] + \mathrm{E}\big[2[w - \mathrm{E}(\hat{w})][\mathrm{E}(\hat{w}) - \hat{w}] \big] \\
  &= \mathrm{Bias}^2(\hat{w}) + \mathrm{Var}(\hat{w})\\
\end{split}
\end{equation}
$$


