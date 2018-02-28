## 高斯马尔科夫定理
用反证法，假设存在比 OLS 更好的无偏线性估计 $\tilde{w}$，$M$ 为任意矩阵，设

$$
\tilde{w} = My
$$

之所以称之为线性估计，是因为 $\tilde{w}$ 是 $y$ 的线性函数，即 $\tilde{w} = f(y)= My$，OLS 也是 $y$ 的线性函数，即 $\hat{w} = g(y)= (X^TX)^{-1}X^Ty$。

可得 $\tilde{w}$ 的期望是

$$
\begin{equation}
\begin{split}
E(\tilde{w}) &= E(My) \\
 &= E[M(Xw+\epsilon)] \\
 &= E(MXw+M\epsilon) \\
 &= E(MXw)
\end{split}
\end{equation}
$$

为了使 $\tilde{w}$ 无偏，即 $E(\tilde{w}) = E(MXw) = E(w) = w$，$MX = I$ 必须恒成立。

由于 $M$ 为任意矩阵，我可以将 $M$ 改写为 $(X^TX)^{-1}X^T + C$，$C$ 是任意矩阵。只要 $M$ 存在，我肯定能找到满足 $(X^TX)^{-1}X^T + C = M$  的  $C$，这里没有任何技术含量，不要想太多。

由于 $MX = I$ 必须恒成立，因此 $CX = 0$，证明如下

$$
\begin{equation}
\begin{split}
(X^TX)^{-1}X^T + C &= M \\
[(X^TX)^{-1}X^T + C]X &= MX \\
[(X^TX)^{-1}X^T + C]X &= I \\
(X^TX)^{-1}X^TX + CX &= I \\
 CX &= 0
\end{split}
\end{equation}
$$

由于 $\tilde{w}$ 无偏，$MX = I$，$\mathrm{E}(\epsilon\epsilon^T)= \sigma^2I$，可得

$$
\begin{equation}
\begin{split}
\mathrm{Var}(\tilde{w}) &= \mathrm{E}\big[ [\tilde{w}-\mathrm{E}(\tilde{w})][\tilde{w}-\mathrm{E}(\tilde{w})]^T \big] \\
 &= \mathrm{E}\big[ (\tilde{w}-w)(\tilde{w}-w)^T \big] \\
 &= \mathrm{E}\big[ [M(Xw+\epsilon)-w][M(Xw+\epsilon)-w]^T \big] \\
 &= \mathrm{E}\big[ (M\epsilon)(M\epsilon)^T \big] \\
 &= \mathrm{E}(M\epsilon\epsilon^TM^T) \\
 &= M\mathrm{E}(\epsilon\epsilon^T)M^T \\
 &= \sigma^2MM^T
\end{split}
\end{equation}
$$

由于 $(X^TX)^{-1}X^T + C = M$，$CX = 0$ 以及 $X^TC^T = 0$，因此

$$
\begin{equation}
\begin{split}
\mathrm{Var}(\tilde{w})
 &= \sigma^2MM^T\\
 &= \sigma^2[(X^TX)^{-1}X^T + C][(X^TX)^{-1}X^T + C]^T\\
 &= \sigma^2\big[ (X^TX)^{-1}X^T[(X^TX)^{-1}X^T]^T + (X^TX)^{-1}X^TC^T + C[(X^TX)^{-1}X^T]^T + CC^T \big]\\
 &= \sigma^2\big[ (X^TX)^{-1} + CC^T \big]
\end{split}
\end{equation}
$$

因为对于任意矩阵 $A$，$AA^T \geq 0$ 恒成立，所以

$$\mathrm{Var}(\tilde{w}) - \mathrm{Var}(\hat{w}) = \sigma^2\big[ (X^TX)^{-1} + CC^T \big] - \sigma^2(X^TX)^{-1} = \sigma^2(CC^T) \geq 0$$

也就是说，$\mathrm{Var}(\tilde{w}) \geq \mathrm{Var}(\hat{w})$，比 $\hat{w}$ 更好的无偏线性估计不存在，因此 OLS 估计是最佳无偏线性估计。