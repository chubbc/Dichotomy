from manim_slide import *
import math

config.background_color = "#161c20"
reponame = "Dichotomy"
arxivnum = "2303.05524"

heading_prev = True

temp = TexTemplate()

temp.add_to_preamble(r"""
\usepackage{stmaryrd,mathtools}
\usepackage{marvosym} \usepackage{fontawesome}

\newcommand{\Tr} {\mathrm{Tr}}

\DeclareFontFamily{U}{mathx}{}
\DeclareFontShape{U}{mathx}{m}{n}{ <-> mathx10 }{}
\DeclareSymbolFont{mathx}{U}{mathx}{m}{n}
\DeclareFontSubstitution{U}{mathx}{m}{n}
\DeclareMathAccent{\widecheck}{0}{mathx}{"71}

\newcommand\Dp{\overline D}
\newcommand\Dm{\widecheck D}
\newcommand\DL{\widetilde D}


\newcommand{\rel}[2]      {\!\left( #1 \middle\| #2 \right)}
\newcommand{\reli}[1]     {\!\left( \rho_{#1} \middle\| \sigma_{#1} \right)}
\newcommand{\pinch}[2]    {\mathcal P_{#2}\!\left(#1\right)}
""")
temp.add_to_document(r"\fontfamily{lmss}\selectfont")

def MyTex(*x,tex_environment="center",tex_template="",color=WHITE,scale=1.0):
    return Tex(*x,
        tex_template=temp,
        tex_environment=tex_environment,
        color=color
    ).scale(scale)

def MyMathTex(*x,tex_environment="align*",color=WHITE,scale=1.0):
    return MyTex(*x,
        tex_environment=tex_environment,
        color=color
    ).scale(scale)

toc=VGroup(
    MyTex(r"1.~Setting \& Results"),
    MyTex(r"2.~Hypothesis testing"),
    MyTex(r"3.~From HT to Blackwell"),
    MyTex(r"4.~Blackwell rates"),
    MyTex(r"5.~Conclusion"),
).arrange(DOWN,buff=0.5,aligned_edge=LEFT).move_to(ORIGIN)

footer=VGroup(
    MyTex(r"\faGithubSquare~$\texttt{chubbc/" + reponame + r"}$"),
    MyTex(r"\faExternalLinkSquare~$\texttt{christopherchubb.com/"+ reponame + r"}$"),
    MyTex(r"\faTwitterSquare~\faYoutubePlay~$\texttt{@QuantumChubb}$"),
).arrange(RIGHT,buff=3).to_corner(DOWN).shift(0.5*DOWN).scale(1/2).set_opacity(.5)

class Title(SlideScene):
    def construct(self):
        title = MyTex(r"\bfseries\textsc{Quantum dichotomies and\\coherent thermodynamics}").scale(1.25).shift(2.75*UP)
        arxiv = MyTex(r"\bfseries\texttt{arXiv:" + arxivnum + r"}").scale(.75).shift(1.75*UP)
        name = MyTex(r"Christopher T.\ Chubb").shift(0.875*UP)
        ethz=SVGMobject("ethz_logo_white.svg").scale(1/4).shift(-0.25*DOWN)
        collab=VGroup(
            MyTex("Joint work with:"),
            MyTex(r"{\bfseries Patryk Lipka-Bartosik} (UNIGE)"),
            MyTex(r"{\bfseries Joe Renes} (ETHZ)"),
            MyTex(r"{\bfseries Marco Tomamichel} (NUS)"),
            MyTex(r"{\bfseries Kamil Korzekwa} (UJ)"),
        ).arrange(DOWN).scale(0.625).shift(1.625*DOWN)
        footer_big=footer.copy().arrange(RIGHT,buff=.375).to_corner(DOWN).shift(0.0*UP).scale(1.25).set_opacity(1)

        self.add(name,title,arxiv,ethz,footer_big,collab)
        # self.slide_break()

        self.play(Unwrite(VGroup(title,arxiv,name,ethz,collab)))
        self.play(ReplacementTransform(footer_big,footer))
        self.slide_break()

        mt=MyTex(r"\bfseries Infomation\\theory").set_color(RED).shift(3.5*LEFT+2*DOWN)
        cc=MyTex(r"\bfseries Quantum\\dichotomies").shift(1.25*DOWN)
        kk=MyTex(r"\bfseries Quantum\\thermodynamics").set_color(BLUE).shift(3.5*RIGHT+2*DOWN)
        arrow=CurvedArrow(start_point=4*LEFT,end_point=4*RIGHT,angle=-PI/3).shift(0.75*UP)
        arrow[0].set_color([BLUE,WHITE,RED]).set_sheen_direction(LEFT)
        arrow[1].set_color(BLUE)
        Group(mt,cc,kk).scale(1.25).shift(2*UP)

        mt2=MyTex(r"Hypothesis\\testing").set_color(RED).shift(1.25*3.5*LEFT)
        cc2=MyTex(r"Blackwell\\order").shift(1*UP)
        kk2=MyTex(r"State\\interconversion").set_color(BLUE).shift(1.25*3.5*RIGHT)
        Group(mt2,cc2,kk2).shift(1.75*DOWN)

        # Group(mt,cc,kk,mt2,cc2,kk2,arrow).shift(DOWN/2)

        self.play(Write(kk))
        self.slide_break()
        self.play(Write(mt))
        self.slide_break()
        self.play(Write(arrow))
        self.play(Write(cc))
        self.slide_break()

        self.play(Write(mt2))
        self.slide_break()
        self.play(Write(cc2))
        self.slide_break()
        self.play(Write(kk2))
        self.slide_break()

        # pics=Group(*[
        #     ImageMobject(name+".jpg").set(height=1.5) for name in ["mt","jr","cc","kk","plb"]
        # ]).arrange(RIGHT,buff=1).move_to(2.5*UP)
        #
        # self.play(FadeIn(pics))
        # self.slide_break()

        # self.play(FadeOut(*[cc,kk,mt,mt_pic,kk_pic,cc_pic,arrow]))
        self.play(FadeOut(*[cc,kk,mt,cc2,kk2,mt2,arrow]))
        self.slide_break()

        self.play(FadeIn(toc))
        self.slide_break()

        self.play(toc[0].animate.scale(1.2).set_color(YELLOW))
        self.slide_break()

        for i in range(1,len(toc)):
           self.play(toc[i].animate.scale(1.2).set_color(YELLOW),toc[i-1].animate.scale(1/1.2).set_color(WHITE))
           self.slide_break()

        self.play(toc[-1].animate.scale(1/1.2).set_color(WHITE))

        tocindex=-1
        if heading_prev:
            self.slide_break()
            heading_next = toc[tocindex+1].copy().move_to(ORIGIN).scale(1.5).to_corner(UP)
            self.remove(toc[tocindex+1])
            self.play(FadeOut(toc[0:tocindex+1]),FadeOut(toc[tocindex+2:]), TransformFromCopy(toc[tocindex+1],heading_next))
            self.wait()

class Results(SlideScene):
    def construct(self):
        tocindex = 0
        heading = toc[tocindex].copy()
        heading.save_state()
        if heading_prev:
            heading.move_to(ORIGIN).scale(1.5).to_corner(UP)
            self.add(heading,footer)
        else:
            self.add(toc[:tocindex],toc[tocindex+1:],footer)
            self.play(FadeOut(toc[:tocindex]),FadeOut(toc[tocindex+1:]),heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

        # heading = toc[tocindex].copy()
        # if heading_prev:
        #     heading.move_to(ORIGIN).scale(1.5).to_corner(UP)
        #     self.add(heading,footer)
        # else:
        #     self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        #     self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
        #     self.slide_break()


        subsec1=subsec2=subsec3=subsec4=False

        subsec1=True
        subsec2=True
        subsec3=True
        subsec4=True

        if subsec1:
            blackwell=MyMathTex(
                r"\rho_1",
                r"\succeq_{}",
                r"\rho_2",
                r"\qquad\quad\iff\quad\qquad",
                r"\exists \mathcal E :~~",
                r"\rho_{1}\mapsto\rho_{2}",
                r"\sigma_{1}\mapsto\sigma_{2}",
            )
            blackwell[:-1].move_to(ORIGIN)
            blackwell[-1].move_to(blackwell[-2]).shift(DOWN/3)
            self.play(Write(blackwell[:3]))
            self.slide_break()

            self.play(Write(blackwell[4:-1]))
            self.play(FadeIn(blackwell[3]))
            self.slide_break()

            self.play(
                Transform(
                    blackwell[0],
                    MyMathTex(r"(\rho_1,\sigma_1)").move_to(blackwell[0],aligned_edge=RIGHT)
                ),
                Transform(
                    blackwell[2],
                    MyMathTex(r"(\rho_2,\sigma_2)").move_to(blackwell[2],aligned_edge=LEFT)
                ),
                blackwell[3].animate.shift(RIGHT/1.5)
            )
            self.play(
                blackwell[5].animate.shift(UP/3),
                FadeIn(blackwell[-1]),
            )
            self.slide_break()

            blackwell_text=MyTex(" ","Blackwell ordering").shift(1.25*UP)
            self.play(FadeIn(blackwell_text))
            self.slide_break()

            x=MyMathTex(
                r"(\rho_1,\sigma_1)",
                r"\succeq_{(\epsilon_\rho,\epsilon_\sigma)}",
                r"(\rho_2,\sigma_2)",
            ).move_to(blackwell[:3])
            self.play(
                Transform(blackwell_text,MyTex("Approximate ","Blackwell ordering").move_to(blackwell_text)),
            )
            self.play(
                blackwell[0].animate.move_to(x[0]),
                Transform(blackwell[1],x[1]),
                blackwell[2].animate.move_to(x[2]),
                blackwell[3].animate.shift(RIGHT/2),
                blackwell[4:].animate.shift(RIGHT/2),
            )
            approx=VGroup(
                MyMathTex(r"\rho_{1}\stackrel{\epsilon_\rho}\mapsto\rho_{2}").move_to(blackwell[-2],aligned_edge=DOWN),
                MyMathTex(r"\sigma_{1}\stackrel{\epsilon_\sigma}\mapsto\sigma_{2}").move_to(blackwell[-1],aligned_edge=DOWN),
            )
            self.play(FadeIn(approx))
            self.remove(blackwell[-2:])
            self.slide_break()

            self.play(
                FadeOut(blackwell),
                FadeOut(approx),
                FadeOut(blackwell_text),
            )
            self.slide_break()

        if subsec2:
            thermo=VGroup(
                MyTex(r"\bfseries Quantum thermodynamics"),
                VGroup(
                    MyTex("Thermal:"),
                    MyMathTex(r"\mathcal E(\rho)=\mathrm{Tr}_2\left[U(\rho\otimes \gamma)U^\dag \right]")
                ).arrange(DOWN),
                VGroup(
                    MyTex("Gibbs-preserving:"),
                    MyMathTex(r"\text{Any }\mathcal E\text{ s.t. }\mathcal E(\gamma)=\gamma")
                ).arrange(DOWN),
                MyMathTex(r"\rho_1 \xrightarrow{\text{GPO}} \rho_2 \quad\iff\quad (\rho_1,\gamma)\succeq (\rho_2,\gamma)"),
            ).set_color(BLUE).scale(0.75)
            thermo[0].move_to(2.25*UP)
            thermo[1].move_to(3*LEFT+1.25*UP)
            thermo[2].move_to(3*RIGHT+1.25*UP)
            thermo[3].move_to(ORIGIN)
            self.play(FadeIn(thermo[0]))
            self.slide_break()
            self.play(FadeIn(thermo[1]))
            self.slide_break()
            self.play(FadeIn(thermo[2]))
            self.slide_break()
            self.play(Write(thermo[3]))
            self.slide_break()

            entanglement=VGroup(
                MyTex(r"\bfseries Entanglement"),
                MyMathTex(r"\left| \phi\right\rangle \xrightarrow{\text{LOCC}} \left| \psi\right\rangle  \quad\iff\quad \left(\mathrm{Tr}_2|\phi\rangle\!\langle\phi|,|0\rangle\!\langle 0|\right)\prec \left(\mathrm{Tr}_2|\psi\rangle\!\langle\psi|,|0\rangle\!\langle 0|\right)"),
            ).scale(0.75).set_color(RED).arrange(DOWN,buff=0).move_to(1.25*DOWN)
            purity=VGroup(
                MyTex(r"\bfseries Purity"),
                MyMathTex(r"\rho_1\xrightarrow{\text{PPO}} \rho_2  \quad\iff\quad (\rho_1,I/d)\succeq (\rho_2,I/d)"),
            ).scale(0.75).set_color(YELLOW).arrange(DOWN,buff=0).move_to(2.5*DOWN)
            self.play(FadeIn(entanglement))
            self.play(FadeIn(purity))
            self.slide_break()

            self.play(FadeOut(thermo),FadeOut(entanglement),FadeOut(purity))
            self.slide_break()

        if subsec3:

            blackwell_rate=MyMathTex(r"\left(\rho_1^{\otimes n},\sigma_1^{\otimes n}\right)\succeq_{(\epsilon_{\rho,n},\epsilon_{\sigma,n})}\left(\rho_2^{\otimes R_nn},\sigma_2^{\otimes R_nn}\right)")
            blackwell_rate.scale(1).shift(2*UP)
            self.play(Write(blackwell_rate))
            self.slide_break()
            # self.play(FadeIn(blackwell_rate))
            # self.slide_break()

            res_prev=VGroup(
                MyTex(r"\bfseries Previous results:"),
                MyTex(r"\textbullet First-order"),
                MyTex(r"\textbullet Second-order (only small+moderate)"),
                MyTex(r"\textbullet Infidelity"),
                MyTex(r"\textbullet Only one-sided errors"),
                MyTex(r"\textbullet Only commuting states"),
            ).scale(0.75).arrange(DOWN,aligned_edge=LEFT).move_to(3.5*LEFT+DOWN).set_color(BLUE)
            res_prev[0].shift(UP/4).match_x(res_prev)

            res_curr=VGroup(
                MyTex(r"\bfseries Our results:"),
                MyTex(r"\textbullet First-order"),
                MyTex(r"\textbullet Second-order (\emph{all} error regimes)"),
                MyTex(r"\textbullet Trace distance"),
                MyTex(r"\textbullet Two-sided errors for free"),
                MyTex(r"\textbullet Non-commuting intputs (mostly tight)"),
                MyTex(r"\textbullet Partial results for general states"),
            ).scale(0.75).arrange(DOWN,aligned_edge=LEFT).move_to(3.5*RIGHT+DOWN).set_color(YELLOW)
            res_curr[0].shift(UP/4).match_x(res_curr)
            res_curr.align_to(res_prev,UP)

            self.play(FadeIn(res_prev[0]),FadeIn(res_curr[0]))
            self.slide_break()
            for i in range(1,5):
                self.play(Write(res_prev[i]))
                self.slide_break()
                self.play(Write(res_curr[i]))
                self.slide_break()
            self.play(Write(res_prev[5]))
            self.slide_break()
            self.play(Write(res_curr[5:]))
            self.slide_break()

            self.play(FadeOut(res_prev),FadeOut(res_curr),FadeOut(blackwell_rate))
            self.slide_break()

        if subsec4:
            notation=MyMathTex(
                r"&\text{Relative entropy: } & ",
                r"D(\rho\|\sigma)~:=&~\mathrm{Tr}\rho(\log \rho-\log \sigma)\\",
                r"&\text{Relative entropy variance: } & ",
                r"V(\rho\|\sigma)~:=&~\mathrm{Tr}\rho(\log \rho-\log \sigma)^2-D(\rho\|\sigma)^2\\",
                r"&\alpha\text{-R\'enyi divergence (Petz): } & ",
                r"\Dp_\alpha(\rho\|\sigma)~:=&~\frac{\log \mathrm{Tr} \rho^\alpha\sigma^{1-\alpha}}{\alpha-1}\\",
                r"&\alpha\text{-R\'enyi divergence (Minimal): } & ",
                r"""\Dm_\alpha(\rho\|\sigma)~:=&~\begin{dcases}
                    \frac{\log\Tr\left(\sqrt\rho\sigma^{\frac{1-\alpha}{\alpha}} \sqrt\rho\right)^\alpha}{\alpha-1} & \alpha\geq 1/2\\
                    \frac{\log\Tr\left(\sqrt\sigma\rho^{\frac{\alpha}{1-\alpha}} \sqrt\sigma\right)^{1-\alpha}}{\alpha-1} & \alpha\leq 1/2
                \end{dcases}\\""",
                r"&\alpha\text{-R\'enyi divergence (Pinched): } & ",
                r"\DL_\alpha(\rho\|\sigma)~:=&~\lim_{n\to\infty} \frac 1n D_\alpha\rel{\pinch{\rho^{\otimes n}}{\sigma^{\otimes n}}}{\sigma^{\otimes n}}",
            ).scale(0.75)
            notation[0:4].shift(0.25*UP).set_color(YELLOW)
            notation[4:6].set_color(RED)
            notation[6:8].set_color(GREEN)
            notation[8:10].set_color(BLUE)
            notation.move_to(0.5*DOWN)
            for i in range(5):
                self.play(FadeIn(notation[2*i:2*i+2]))
                self.slide_break()

            self.play(FadeOut(notation))
            self.slide_break()

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), Restore(heading))
        if heading_prev:
            self.slide_break()
            heading_next = toc[tocindex+1].copy().move_to(ORIGIN).scale(1.5).to_corner(UP)
            self.remove(toc[tocindex+1])
            self.play(FadeOut(toc[:tocindex]),FadeOut(heading),FadeOut(toc[tocindex+2:]), TransformFromCopy(toc[tocindex+1],heading_next))
            self.wait()

class HT(SlideScene):
    def construct(self):
        tocindex = 1

        heading = toc[tocindex].copy()
        heading.save_state()
        if heading_prev:
            heading.move_to(ORIGIN).scale(1.5).to_corner(UP)
            self.add(heading,footer)
        else:
            self.add(toc[:tocindex],toc[tocindex+1:],footer)
            self.play(FadeOut(toc[:tocindex]),FadeOut(toc[tocindex+1:]),heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

        subsec1=subsec2=subsec3=False

        subsec1=True
        subsec2=True
        subsec3=True

        if subsec1:
            v=np.random.rand(100)
            v.sort()
            v=1-np.cumsum(v[-1::-1]/sum(v))

            ht=VGroup(
                MyTex(r"We want to test between two states $\rho$ and $\sigma$:"),
                MyMathTex(r"\alpha(T):=\Tr\rho(I-T)\qquad \beta(T):=\Tr\sigma T")
            ).arrange(DOWN,buff=1)

            self.play(FadeIn(ht[0]))
            self.slide_break()
            self.play(Write(ht[1]))
            self.slide_break()
            self.play(
                ht[0].animate.shift(1.5*UP),
                ht[1].animate.shift(2*UP)
            )
            self.slide_break()

            axes=Axes(
                x_range=[0,1,1],
                y_range=[0,1,1],
                x_length=6,
                y_length=6,
                z_index=+2,
            ).scale(0.5).shift(DOWN)
            axis_labels=axes.get_axis_labels(x_label=r"\alpha",y_label=r"\beta")

            self.play(FadeIn(axes),FadeIn(axis_labels))
            self.slide_break()

            x=np.array([])
            y=np.array([])
            for i in range(1000):
                xx=0.0
                yy=0.0
                while (xx+1)*(yy+1)<=2.01:
                    xx=0.99*np.random.rand()
                    yy=0.99*np.random.rand()
                x=np.append(x,xx)
                y=np.append(y,yy)

            pts=VGroup(*[
                Circle(0.02,color=BLUE,fill_opacity=1).move_to(axes.coords_to_point(x[i],y[i])) for i in range(1000)
            ])

            X=[i/100 for i in range(101)]
            Y=[2/(i/100+1)-1 for i in range(101)]
            region=Polygon(
                axes.coords_to_point(1,1),
                *[axes.coords_to_point(X[i],Y[i]) for i in range(101)],
                color=BLUE,
                z_index=+1,
                fill_opacity=1.0,
            )

            self.play(FadeIn(pts[0]))
            self.slide_break()

            self.play(FadeIn(pts[1]))
            self.slide_break()

            k=100
            self.play(AnimationGroup(
                *[FadeIn(pts[i],run_time=1/i) for i in range(2,k)],
                lag_ratio=1,
            ))
            animgrp=AnimationGroup(
                AnimationGroup( *[FadeIn(pts[i]) for i in range(k,1000)], run_time=3, lag_ratio=0.9 ),
                FadeIn(region, run_time=3)
            )
            self.play(animgrp)
            self.remove(*pts)
            self.slide_break()

            lorenz=axes.plot_line_graph(
                x_values = X,
                y_values = Y,
                vertex_dot_radius=0,
                # line_color=GRAY,
                line_color=BLUE,
                stroke_width = 3,
            )
            self.play(FadeOut(region),FadeIn(lorenz))
            self.slide_break()

            self.play(VGroup(axes,axis_labels,lorenz).animate.shift(3*LEFT))
            self.slide_break()

            beta=MyMathTex(r"\beta_x\reli{}:=\min_{T}\left\lbrace \mathrm{Tr} \sigma T \middle| \mathrm{Tr} \rho T \geq 1-x  \right\rbrace").set_color(BLUE).shift(2.75*RIGHT+DOWN).scale(0.9)
            self.play(Write(beta))
            self.slide_break()

            self.play(FadeOut(ht),FadeOut(VGroup(axes,axis_labels,lorenz)),FadeOut(beta))
            self.slide_break()

        if subsec2:
            asymp=MyTex(r"What if $n\to\infty$?").shift(2*UP)
            self.play(FadeIn(asymp))
            self.slide_break()

            stein=VGroup(
                MyTex(r"\bfseries Stein's lemma"),
                MyMathTex(r"\alpha_n=\text{const.} \qquad \implies \qquad \beta_{n}\sim e^{-D\reli{}n}"),
                MyMathTex(r"\lim_{n\to\infty} -\frac 1n \log \beta_\epsilon\rel{\rho^{\otimes n}}{\sigma^{\otimes n}}=D\reli{}"),
            ).shift(DOWN)
            stein[0].move_to(UP/2)
            self.play(FadeIn(stein[0]))
            self.slide_break()
            self.play(FadeIn(stein[1]))
            self.slide_break()
            self.play(FadeOut(stein[1]),FadeIn(stein[2]))
            self.slide_break()

            self.play(FadeOut(asymp),FadeOut(stein[0]),FadeOut(stein[2]))
            self.slide_break()

        if subsec3:
            ax=Axes(
                x_range=[0,10,10],
                y_range=[0,1,1],
                x_length=20,
                y_length=8,
                axis_config={
                    "include_tip": True,
                    "include_numbers": False,
                    "numbers_to_exclude": [r for r in range(3,25) if np.mod(r,5)!=0]
                },
            ).scale(0.5)
            axis_labels=MyMathTex(r"-\frac 1n \log \beta_n", r"\alpha_n").scale(0.75)
            axis_labels[0].next_to(ax,DOWN).shift(3*RIGHT)
            axis_labels[1].rotate(90*DEGREES).next_to(ax,LEFT)

            x=np.arange(-5,5,0.1)
            n=6
            l = Group(*[
                ax.plot_line_graph(
                    x_values = x+5,
                    y_values = 1/(1+np.exp(-2**(i-2)*x)),
                    vertex_dot_radius=0,
                    # line_color=GRAY,
                    line_color=rgb_to_color(((i+2)/(n+1),(i+2)/(n+1),(i+2)/(n+1))),
                    stroke_width = 3,
                ) for i in range(n)
            ])
            th=(ax.plot_line_graph(
                x_values = [5,5],
                y_values = [0,1],
                vertex_dot_radius=0,
                line_color=WHITE,
                stroke_width = 5,
            ))

            self.play(FadeIn(ax),FadeIn(axis_labels))
            self.slide_break()

            for ll in l[:2]:
                self.play(Write(ll))
                self.slide_break()
            for ll in l[2:]:
                self.play(Write(ll,run_time=1))
            # self.slide_break()
            self.play(Write(th))
            rel_ent=MyMathTex(r"D\reli{}").next_to(ax,DOWN).scale(0.75)
            self.play(Write(rel_ent))
            self.slide_break()


            large_array_1 = np.uint8(
                [[(255,255,0,(x/128+(x>128)*(1-x/128))*y/1.5) for x in range(0, 256)] for y in range(0, 256)]
            )
            large_array_2 = np.uint8(
                [[(255,255,0,((x<128)*(x/128)+(x>=128)*(2-x/128))*y/1.5) for x in range(0, 256)] for y in range(0, 256)]
            )
            largedev=Group(
                ImageMobject(large_array_1[:,-1::-1]).stretch_to_fit_width(5).stretch_to_fit_height(.75).move_to(ax.coords_to_point(0,0),aligned_edge=LEFT+DOWN),
                ImageMobject(large_array_2[-1::-1,:]).stretch_to_fit_width(5).stretch_to_fit_height(.75).move_to(ax.coords_to_point(10,1),aligned_edge=RIGHT+UP),
            )
            small_array = np.uint8(np.concatenate((
                [[(75,75,255,255*(1-x/256)**1*(1-abs(y/128-1)**2)) for x in range(255, -1, -1)] for y in range(0, 256)],
                [[(75,75,255,255*(1-x/256)**1*(1-abs(y/128-1)**2)) for x in range(0, 256)] for y in range(0, 256)],
            ),axis=1))
            smalldev=ImageMobject(small_array).stretch_to_fit_width(1.5).stretch_to_fit_height(4).move_to(ax.coords_to_point(5,0.5))
            mod_array = np.uint8(
                [[(0,150,0,(x+y>255)*(x+y)) for x in range(0, 256)] for y in range(0, 256)]
            )
            moddev=Group(
                ImageMobject(mod_array).stretch_to_fit_width(2).stretch_to_fit_height(2).move_to(ax.coords_to_point(5,0),aligned_edge=DOWN+RIGHT),
                ImageMobject(mod_array[-1::-1,-1::-1]).stretch_to_fit_width(2).stretch_to_fit_height(2).move_to(ax.coords_to_point(5,1),aligned_edge=UP+LEFT),
            )
            ext_array = np.uint8(
                [[(255,0,0,(x+y>255)*(x+y)) for x in range(0, 256)] for y in range(0, 256)]
            )
            extdev=ImageMobject(ext_array[-1::-1,:]).stretch_to_fit_width(2).stretch_to_fit_height(1).move_to(ax.coords_to_point(9.9,1),aligned_edge=UP+RIGHT)

            smalldev.z_index=-1
            largedev.z_index=-1
            moddev.z_index=-1
            extdev.z_index=-1

            smallarrow=VGroup(
                Arrow(start=ax.coords_to_point(3.75,0.25),end=ax.coords_to_point(5,0.25)),
                Arrow(start=ax.coords_to_point(3.75,0.375),end=ax.coords_to_point(5,0.375)),
                Arrow(start=ax.coords_to_point(6.25,0.625),end=ax.coords_to_point(5,0.625)),
                Arrow(start=ax.coords_to_point(6.25,0.75),end=ax.coords_to_point(5,0.75)),
            ).set_color(BLUE)

            largearrow=VGroup(
                Arrow(start=ax.coords_to_point(1,0.3),end=ax.coords_to_point(1,0)),
                Arrow(start=ax.coords_to_point(2,0.3),end=ax.coords_to_point(2,0)),
                Arrow(start=ax.coords_to_point(8,0.7),end=ax.coords_to_point(8,1)),
                Arrow(start=ax.coords_to_point(9,0.7),end=ax.coords_to_point(9,1)),
            ).set_color(YELLOW)

            modarrow=VGroup(
                Arrow(start=ax.coords_to_point(3.5,0.25),end=ax.coords_to_point(5,0)),
                Arrow(start=ax.coords_to_point(6.5,0.75),end=ax.coords_to_point(5,1)),
            ).set_color(rgb_to_color((0,0.75,0)))

            extarrow=Arrow(start=ax.coords_to_point(8.5,0.75),end=ax.coords_to_point(10,1)).set_color(rgb_to_color((1,0,0)))

            self.play(*[Write(x) for x in smallarrow])
            self.slide_break()
            self.play(FadeOut(smallarrow),FadeIn(smalldev))
            self.slide_break()

            self.play(*[Write(x) for x in largearrow])
            self.slide_break()
            self.play(FadeOut(largearrow),FadeIn(largedev))
            self.slide_break()

            self.play(*[Write(x) for x in modarrow])
            self.slide_break()
            self.play(Write(extarrow))
            self.slide_break()
            self.play(FadeOut(modarrow),FadeOut(extarrow),FadeIn(moddev),FadeIn(extdev))
            self.slide_break()

            sigmoid=Group(ax,axis_labels,l,th,smalldev,largedev,moddev,extdev,rel_ent)
            self.play(sigmoid.animate.scale(0.625).shift(3*LEFT+UP))
            self.slide_break()

            tab = MobjectTable(
                [
                    [MyTex("Exp small"), MyMathTex(r"[0,D)")],
                    [MyTex("Subexp small"), MyMathTex(r"D-\omega(1/\sqrt n)\cap o(1)")],
                    [MyTex(r"Const ($<0.5$)"), MyMathTex(r"D- \Theta(1/\sqrt n)")],
                    [MyTex(r"Const ($>0.5$)"), MyMathTex(r"D+ \Theta(1/\sqrt n)")],
                    [MyTex("Subexp large"), MyMathTex(r"D+\omega(1/\sqrt n)\cap o(1)")],
                    [MyTex("Exp large"), MyMathTex(r"(D,\infty)")],
                    [MyTex("Superexp large"), MyMathTex(r"\infty")],
                ],
                row_labels=[
                    MyTex("Lrg$_<$"),
                    MyTex("Mod$_<$"),
                    MyTex("Sml$_<$"),
                    MyTex("Sml$_>$"),
                    MyTex("Mod$_>$"),
                    MyTex("Lrg$_>$"),
                    MyTex("Ext")
                ],
                col_labels=[MyMathTex(r"\alpha_n"), MyMathTex(r"-\frac 1n \log \beta_n")],
                include_outer_lines=False,
                line_config={"stroke_width": 1},
                v_buff=0.5,
            ).scale(0.4).shift(3.5*RIGHT+1*UP)

            tab[1].set(stroke_width=2)
            # tab[4].set(stroke_width=2)
            tab[8].set(stroke_width=2)
            tab[0][8:14].set_color(BLUE)
            tab[0][5:8].set_color(GREEN)
            tab[0][14:17].set_color(GREEN)
            tab[0][2:5].set_color(YELLOW)
            tab[0][17:20].set_color(YELLOW)
            tab[0][20:].set_color(RED)

            self.play(Write(tab[1]),Write(tab[4]),Write(tab[8]))
            self.play(FadeIn(tab[0][0:2]))
            self.play(*[FadeIn(tab[0][2+3*i]) for i in range(7)])
            self.slide_break()

            self.play(FadeIn(tab[0][9:11]),FadeIn(tab[0][12:14]))
            self.slide_break()
            eqn=MyMathTex(r"-\frac 1n \log \beta_n(\epsilon)\simeq D\reli{}+\sqrt{\frac{2V\reli{}}n}\Phi^{-1}(\epsilon)",color=BLUE,scale=0.75).move_to(2.5*DOWN)
            self.play(Write(eqn))
            self.slide_break()

            self.play(FadeOut(eqn),FadeIn(tab[0][3:5]),FadeIn(tab[0][18:20]))
            # self.slide_break()
            eqn=MyMathTex(
                r"-\frac 1n \log \beta_n(e^{-\lambda n})&\simeq \sup_{t\in (0,1)} \Dp_t\reli{}+\frac{t}{1-t}\lambda\\",
                r"-\frac 1n \log \beta_n(1-e^{-\lambda n})&\simeq\inf_{t>1} \Dm_t\reli{}-\frac t{1-t}\lambda",
                color=YELLOW,scale=0.75).move_to(2.5*DOWN)
            self.play(Write(eqn))
            self.slide_break()

            self.play(FadeOut(eqn),FadeIn(tab[0][6:8]),FadeIn(tab[0][15:17]))
            # self.slide_break()
            eqn=MyMathTex(
                r"-\frac 1n \log \beta_n(e^{-\lambda n^a})&\simeq D\reli{}-\sqrt{2V\reli{}\cdot\lambda n^{a-1}}\\",
                r"-\frac 1n \log \beta_n(1-e^{-\lambda n^a})&\simeq D\reli{}+\sqrt{2V\reli{}\cdot\lambda n^{a-1}}",
                color=GREEN,scale=0.75).move_to(2.5*DOWN)
            self.play(Write(eqn))
            self.slide_break()

            self.play(FadeOut(eqn),FadeIn(tab[0][21:]))
            # self.slide_break()
            eqn=MyMathTex(r"-\frac 1n \log \beta_n(1-e^{-\lambda n})\simeq \lambda-D_{\mathrm{max}}\reli{}",color=RED,scale=0.75).move_to(2.5*DOWN)
            self.play(Write(eqn))
            self.slide_break()

            self.play(
                FadeOut(sigmoid),
                FadeOut(eqn),
                FadeOut(tab[0:2]),
                FadeOut(tab[4]),
                FadeOut(tab[8])
            )
            self.slide_break()

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), Restore(heading))
        if heading_prev:
            self.slide_break()
            heading_next = toc[tocindex+1].copy().move_to(ORIGIN).scale(1.5).to_corner(UP)
            self.remove(toc[tocindex+1])
            self.play(FadeOut(toc[:tocindex]),FadeOut(heading),FadeOut(toc[tocindex+2:]), TransformFromCopy(toc[tocindex+1],heading_next))
            self.wait()

class Reduction(SlideScene):
    def construct(self):
        tocindex = 2
        heading = toc[tocindex].copy()
        heading.save_state()
        if heading_prev:
            heading.move_to(ORIGIN).scale(1.5).to_corner(UP)
            self.add(heading,footer)
        else:
            self.add(toc[:tocindex],toc[tocindex+1:],footer)
            self.play(FadeOut(toc[:tocindex]),FadeOut(toc[tocindex+1:]),heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

        subsec1=subsec2=False

        subsec1=True
        subsec2=True

        if subsec1:
            when=MyTex(r"When does ",r"$(\rho_1,\sigma_1)$ ",r" $\succeq$",r" $(\rho_2,\sigma_2)$","?")
            when[1].set_color(BLUE)
            when[3].set_color(RED)
            self.play(Write(when))
            self.slide_break()

            dpi=MyMathTex(r"Q",r"(\rho_1",r",",r"\sigma_1)",r"\geq ",r"Q",r"(\rho_2",r",",r"\sigma_2)")
            dpi[:4].set_color(BLUE)
            dpi[5:].set_color(RED)
            dpi.shift(DOWN)
            self.play(when.animate.shift(UP))
            self.play(FadeIn(dpi))
            self.slide_break()

            newdpi=MyMathTex(r"D",r"(\rho_1",r"\|",r"\sigma_1)",r"\geq ",r"D",r"(\rho_2",r"\|",r"\sigma_2)")
            newdpi[:4].set_color(BLUE)
            newdpi[5:].set_color(RED)
            newdpi.shift(dpi[4].get_center()-newdpi[4].get_center())
            self.play(Transform(dpi,newdpi))
            self.slide_break()

            newdpi=MyMathTex(r"\Dp_\alpha",r"(\rho_1",r"\|",r"\sigma_1)", r"\geq ",r"\Dp_\alpha",r"(\rho_2",r"\|",r"\sigma_2)")
            newdpi[:4].set_color(BLUE)
            newdpi[5:].set_color(RED)
            newdpi.shift(dpi[4].get_center()-newdpi[4].get_center())
            self.play(Transform(dpi,newdpi))
            self.slide_break()

            newdpi=MyMathTex(r"\Dm_\alpha",r"(\rho_1",r"\|",r"\sigma_1)",r"\geq ",r"\Dm_\alpha",r"(\rho_2",r"\|",r"\sigma_2)")
            newdpi[:4].set_color(BLUE)
            newdpi[5:].set_color(RED)
            newdpi.shift(dpi[4].get_center()-newdpi[4].get_center())
            self.play(Transform(dpi,newdpi))
            self.slide_break()

            newdpi=MyMathTex(r"\beta_x",r"(\rho_1",r"\|",r"\sigma_1)",r"\leq ",r"\beta_x",r"(\rho_2",r"\|",r"\sigma_2)")
            newdpi[:4].set_color(BLUE)
            newdpi[5:].set_color(RED)
            newdpi.shift(dpi[4].get_center()-newdpi[4].get_center())
            self.play(Transform(dpi,newdpi))
            self.slide_break()

            olddpi=dpi
            dpi=MyMathTex(r"\beta_x",r"(\rho_1",r"\|",r"\sigma_1)",r"\leq ",r"\beta_x",r"(\rho_2",r"\|",r"\sigma_2)",r" ",r"~~\forall x")
            dpi[:4].set_color(BLUE)
            dpi[5:-1].set_color(RED)
            dpi.shift(olddpi[4].get_center()-dpi[4].get_center())
            self.remove(olddpi)
            self.add(dpi[:-1])
            self.play(FadeIn(dpi[-1:]))
            self.slide_break()
            iff=MyMathTex(r"\iff").rotate(-PI/2)
            self.play(FadeIn(iff))
            self.slide_break()

            # oldwhen=when
            newwhen=MyTex(r"When does ",r"$(\rho_1,\sigma_1)$ ",r" $\succeq_{(\epsilon_\rho,\epsilon_\sigma)}$",r" $(\rho_2,\sigma_2)$","?").shift(UP)
            newwhen[1].set_color(BLUE)
            newwhen[3].set_color(RED)
            # olddpi=dpi
            newdpi=MyMathTex(
                r"\beta_x",
                r"(\rho_1",
                r"\|",
                r"\sigma_1)",
                r"\leq ",
                r"\beta_{x-\epsilon_\rho}",
                r"(\rho_2",
                r"\|",
                r"\sigma_2)",
                r"+\epsilon_\sigma",
                r"~~\forall x").shift(DOWN)
            newdpi[:4].set_color(BLUE)
            newdpi[5:-1].set_color(RED)
            # oldiff=iff
            self.play(Transform(when,newwhen),Transform(dpi,newdpi))
            self.slide_break()

            newiff=MyMathTex(r"\implies").rotate(-PI/2)
            self.play(Transform(iff,newiff))
            self.slide_break()

            self.play(FadeOut(iff),FadeOut(when),dpi.animate.shift(2*DOWN))
            self.slide_break()

            n=1000
            X=np.linspace(0,1,n+1)
            Y1=np.random.rand(n+1)
            Y2=np.random.rand(n+1)
            for i in range(900):
                Y1[i]=Y1[i]/8
            for i in range(400):
                Y2[i]=Y2[i]/20
            Y1=1-np.cumsum(np.flip(np.sort(Y1/sum(Y1))))
            Y2=1-np.cumsum(np.flip(np.sort(Y2/sum(Y2))))
            Y1[0]=Y2[0]=1

            ax=Axes(
                x_range=[0,1,1],
                y_range=[0,1,1],
                x_length=8,
                y_length=8,
            ).scale(0.5)#.shift(UP)
            # axis_labels=axes.get_axis_labels(x_label=r"\alpha",y_label=r"\beta")

            lc1=ax.plot_line_graph(
                x_values = X,
                y_values = Y1,
                vertex_dot_radius=0,
                line_color=BLUE,
                stroke_width = 3,
            )

            lc2=ax.plot_line_graph(
                x_values = X,
                y_values = Y2,
                vertex_dot_radius=0,
                line_color=RED,
                stroke_width = 3,
            )

            lcd=VGroup(*[
                ax.plot_line_graph(
                    x_values = X[25*i:25*i+15],
                    y_values = Y2[25*i:25*i+15],
                    vertex_dot_radius=0,
                    line_color=RED,
                    stroke_width = 3,
                ) for i in range(40)
            ])

            self.play(Write(ax))
            self.play(Write(lc1),Write(lc2))
            self.add(lcd)
            self.slide_break()

            AX_ORIGIN=lc2.get_center()
            AX_RIGHT=ax.coords_to_point(1,0)-ax.coords_to_point(0,0)
            AX_UP=ax.coords_to_point(0,1)-ax.coords_to_point(0,0)

            ix=0
            x=ix/(n+1)
            y=max([Y1[i+ix]-Y2[i] for i in range(n+1-ix)])
            self.play(lc2.animate.move_to(AX_ORIGIN+x*AX_RIGHT+y*AX_UP))
            self.slide_break()

            brace_v=BraceBetweenPoints(ax.coords_to_point(1,0),ax.coords_to_point(1,y)).set_color(YELLOW)
            brace_v_lab=MyMathTex(r"\epsilon_\sigma").set_color(YELLOW).scale(0.75).next_to(brace_v,buff=0.1)
            brace_v_lab.add_updater(lambda mobject: mobject.next_to(brace_v,buff=0.1))

            self.play(Write(brace_v))
            self.play(FadeIn(brace_v_lab))
            self.slide_break()

            ix=50
            x=ix/(n+1)
            y=max([Y1[i+ix]-Y2[i] for i in range(n+1-ix)])
            self.play(
                lc2.animate.move_to(AX_ORIGIN+x*AX_RIGHT+y*AX_UP),
                Transform(brace_v,BraceBetweenPoints(ax.coords_to_point(1,0),ax.coords_to_point(1,y)).set_color(YELLOW)),
            )
            self.slide_break()

            brace_h=BraceBetweenPoints(ax.coords_to_point(x,1),ax.coords_to_point(0,1)).set_color(YELLOW)
            brace_h_lab=MyMathTex(r"\epsilon_\rho").set_color(YELLOW).scale(0.75).next_to(brace_h,UP,buff=0.1)
            brace_h_lab.add_updater(lambda mobject: mobject.next_to(brace_h,UP,buff=0.1))
            self.play(Write(brace_h))
            self.play(FadeIn(brace_h_lab))
            self.slide_break()

            ix=100
            x=ix/(n+1)
            y=max([Y1[i+ix]-Y2[i] for i in range(n+1-ix)])
            self.play(
                lc2.animate.move_to(AX_ORIGIN+x*AX_RIGHT+y*AX_UP),
                Transform(brace_v,BraceBetweenPoints(ax.coords_to_point(1,0),ax.coords_to_point(1,y)).set_color(YELLOW)),
                Transform(brace_v,BraceBetweenPoints(ax.coords_to_point(1,0),ax.coords_to_point(1,y)).set_color(YELLOW)),
                Transform(brace_h,BraceBetweenPoints(ax.coords_to_point(x,1),ax.coords_to_point(0,1)).set_color(YELLOW)),
            )
            self.slide_break()

            brace_h_lab.clear_updaters()
            brace_h_lab.clear_updaters()

            self.play(VGroup(ax,lc1,lc2,lcd,brace_h,brace_v,brace_h_lab,brace_v_lab).animate.shift(3*LEFT))
            ax_err=Axes(
                x_range=[0,.3,.3],
                y_range=[0,.2,.2],
                x_length=8,
                y_length=8,
            ).scale(0.5).shift(3*RIGHT).set_color(YELLOW)
            self.play(Write(ax_err))
            self.slide_break()

            AX_ORIGIN=lcd.get_center()

            err_labs=VGroup(
                MyMathTex(r"\epsilon_\rho").scale(1).move_to(ax_err.coords_to_point(0.1,-0.02)),
                MyMathTex(r"\epsilon_\sigma").scale(1).rotate(PI/2).move_to(ax_err.coords_to_point(-0.02,0.1)),
            ).set_color(YELLOW)
            self.play(
                ReplacementTransform(VGroup(brace_h,brace_h_lab),err_labs[0]),
                ReplacementTransform(VGroup(brace_v,brace_v_lab),err_labs[1]),
            )

            err_pts=VGroup()
            err_pts+=Circle(radius=0.05,color=YELLOW,fill_opacity=1).move_to(ax_err.coords_to_point(x,y))
            self.play(Flash(err_pts[-1]),FadeIn(err_pts[-1]))
            self.slide_break()

            for ix in [50,150]:
                x=ix/(n+1)
                y=max([Y1[i+ix]-Y2[i] for i in range(n+1-ix)])
                self.play(
                    lc2.animate.move_to(AX_ORIGIN+x*AX_RIGHT+y*AX_UP),
                )
                self.slide_break()

                err_pts+=Circle(radius=0.05,color=YELLOW,fill_opacity=1).move_to(ax_err.coords_to_point(x,y))
                self.play(Flash(err_pts[-1]),FadeIn(err_pts[-1]))
                print((x,y))
                self.slide_break()

            nn=250
            xx=[i/(n+1) for i in range(1,nn)]
            yy=[max([Y1[i+ix]-Y2[i] for i in range(n+1-ix)]) for ix in range(1,nn)]

            err_line=ax_err.plot_line_graph(
                x_values = xx[:1],
                y_values = yy[:1],
                vertex_dot_radius=0,
                line_color=YELLOW,
                stroke_width = 2,
            )
            # self.add(err_line)
            # self.play(FadeIn(err_line),FadeOut(err_pts))
            # self.slide_break()

            self.play(FadeOut(err_pts))
            x=0
            y=max(Y1-Y2)
            self.play(
                lc2.animate.move_to(AX_ORIGIN+x*AX_RIGHT+y*AX_UP),
            )
            circ=Circle(radius=0.05,color=YELLOW,fill_opacity=1,z_index=+1).move_to(ax_err.coords_to_point(x,y))
            self.play(FadeIn(circ))
            self.slide_break()

            for it in range(1,nn,2):
                x=it/(n+1)
                y=max([Y1[i+it]-Y2[i] for i in range(n+1-it)])
                if y<0:
                    break
                self.remove(err_line)
                err_line=ax_err.plot_line_graph(
                    x_values = xx[:it],
                    y_values = yy[:it],
                    vertex_dot_radius=0,
                    line_color=YELLOW,
                    stroke_width = 2,
                )
                self.add(err_line)
                self.play(
                    lc2.animate.move_to(AX_ORIGIN+x*AX_RIGHT+y*AX_UP),
                    circ.animate.move_to(ax_err.coords_to_point(x,y)),
                    run_time=0.05,
                    rate_func=linear,
                )
            self.slide_break()

            self.play(
                FadeOut(VGroup(ax,lc1,lc2,lcd)),
                FadeOut(ax_err),
                FadeOut(*err_line),
                FadeOut(err_labs),
                FadeOut(circ),
            )
            self.slide_break()

            self.play(dpi.animate.shift(2.5*UP))
            noncomm=MyTex("What about non-commuting?").shift(0.5*UP)
            self.play(Write(noncomm))
            self.slide_break()
            violence=MyTex("The only solution is ","violence").shift(1.5*DOWN)
            violence[1].set_color(YELLOW)
            self.play(Write(violence))
            self.slide_break()

            self.play(FadeOut(dpi),FadeOut(noncomm),FadeOut(violence))
            self.slide_break()

        if subsec2:

            whatif=MyTex(r"What if we {\itshape\bfseries make} the states commute?")
            self.play(Write(whatif))
            self.slide_break()

            pinch_meme=ImageMobject("pinch_meme.jpg").set(height=4).shift(DOWN)
            self.play(whatif.animate.shift(2*UP))
            self.play(FadeIn(pinch_meme))
            self.slide_break()

            self.play(FadeOut(pinch_meme))
            self.slide_break()

            pinch=VGroup()
            pinch+=MyMathTex(r"\beta_x\reli{1}",r"\leq ",r"\beta_{x-\epsilon_\rho}\reli{2}+\epsilon_\sigma",r"~~\forall x")
            pinch[-1][0].set_color(BLUE)
            pinch[-1][2].set_color(RED)
            pinch+=MyMathTex(r"\impliedby").rotate(-PI/2)
            pinch+=MyMathTex(r"(\rho_1,\sigma_1)",r"\succeq_{(\epsilon_\rho,\epsilon_\sigma)} ",r"(\rho_2,\sigma_2)")
            pinch[-1][0].set_color(BLUE)
            pinch[-1][2].set_color(RED)
            pinch+=MyMathTex(r"\impliedby").rotate(-PI/2)
            pinch+=MyMathTex(r"\beta_x\rel{\mathcal P_{\sigma_1}(\rho_1)}{\sigma_1}",r"\leq ",r"\beta_{x-\epsilon_\rho}\reli{2}+\epsilon_\sigma",r"~~\forall x")
            pinch[-1][0].set_color(BLUE)
            pinch[-1][2].set_color(RED)
            pinch.arrange(DOWN).shift(DOWN)
            self.play(Write(pinch[0]))
            self.slide_break()
            self.play(Write(pinch[2]),FadeIn(pinch[1]))
            self.slide_break()
            self.play(Write(pinch[4]),FadeIn(pinch[3]))
            self.slide_break()

            self.play(FadeOut(whatif),FadeOut(pinch))
            self.slide_break()

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), Restore(heading))
        if heading_prev:
            self.slide_break()
            heading_next = toc[tocindex+1].copy().move_to(ORIGIN).scale(1.5).to_corner(UP)
            self.remove(toc[tocindex+1])
            self.play(FadeOut(toc[:tocindex]),FadeOut(heading),FadeOut(toc[tocindex+2:]), TransformFromCopy(toc[tocindex+1],heading_next))
            self.wait()

class Rates(SlideScene):
    def construct(self):
        tocindex = 3
        heading = toc[tocindex].copy()
        heading.save_state()
        if heading_prev:
            heading.move_to(ORIGIN).scale(1.5).to_corner(UP)
            self.add(heading,footer)
        else:
            self.add(toc[:tocindex],toc[tocindex+1:],footer)
            self.play(FadeOut(toc[:tocindex]),FadeOut(toc[tocindex+1:]),heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

        ax=Axes(
            x_range=[0,10,10],
            y_range=[0,1,1],
            x_length=20,
            y_length=8,
            axis_config={
                "include_tip": True,
                "include_numbers": False,
                "numbers_to_exclude": [r for r in range(3,25) if np.mod(r,5)!=0]
            },
        ).scale(0.5)
        axis_labels=MyMathTex(r"R_n", r"\epsilon_n").scale(0.75)
        axis_labels[0].next_to(ax,DOWN).shift(3*RIGHT)
        axis_labels[1].rotate(90*DEGREES).next_to(ax,LEFT)

        x=np.arange(-4,5,0.1)
        n=6
        l = Group(*[
            ax.plot_line_graph(
                x_values = x+5,
                y_values = (1-np.exp(1*(-4-x)))/(1+np.exp(-2**(i-2)*x)),
                vertex_dot_radius=0,
                # line_color=GRAY,
                line_color=rgb_to_color(((i+2)/(n+1),(i+2)/(n+1),(i+2)/(n+1))),
                stroke_width = 3,
            ) for i in range(n)
        ])
        th=(ax.plot_line_graph(
            x_values = [5,5],
            y_values = [0,1],
            vertex_dot_radius=0,
            line_color=WHITE,
            stroke_width = 5,
        ))

        self.play(FadeIn(ax),FadeIn(axis_labels))
        self.slide_break()

        for ll in l:
            self.play(Write(ll,run_time=1))
        # self.slide_break()
        self.play(Write(th))
        rel_ent=MyMathTex(r"C=\frac{D\reli{1}}{D\reli{2}}").scale(0.75).next_to(ax,DOWN,buff=0.1).scale(0.75)
        self.play(Write(rel_ent))
        self.slide_break()


        large_array_1 = np.uint8(
            [[(255,255,0,(x/128+(x>128)*(1-x/128))*y/1.5) for x in range(0, 256)] for y in range(0, 256)]
        )
        large_array_2 = np.uint8(
            [[(255,255,0,((x<128)*(x/128)+(x>=128)*(2-x/128))*y/1.5) for x in range(0, 256)] for y in range(0, 256)]
        )
        largedev=Group(
            ImageMobject(large_array_2[:,-1::-1]).stretch_to_fit_width(4).stretch_to_fit_height(.75).move_to(ax.coords_to_point(1,0),aligned_edge=LEFT+DOWN),
            ImageMobject(large_array_1[-1::-1,:]).stretch_to_fit_width(5).stretch_to_fit_height(.75).move_to(ax.coords_to_point(10,1),aligned_edge=RIGHT+UP),
        )
        small_array = np.uint8(np.concatenate((
            [[(75,75,255,255*(1-x/256)**1*(1-abs(y/128-1)**2)) for x in range(255, -1, -1)] for y in range(0, 256)],
            [[(75,75,255,255*(1-x/256)**1*(1-abs(y/128-1)**2)) for x in range(0, 256)] for y in range(0, 256)],
        ),axis=1))
        smalldev=ImageMobject(small_array).stretch_to_fit_width(1.5).stretch_to_fit_height(4).move_to(ax.coords_to_point(5,0.5))
        mod_array = np.uint8(
            [[(0,150,0,(x+y>255)*(x+y)) for x in range(0, 256)] for y in range(0, 256)]
        )
        moddev=Group(
            ImageMobject(mod_array).stretch_to_fit_width(2).stretch_to_fit_height(2).move_to(ax.coords_to_point(5,0),aligned_edge=DOWN+RIGHT),
            ImageMobject(mod_array[-1::-1,-1::-1]).stretch_to_fit_width(2).stretch_to_fit_height(2).move_to(ax.coords_to_point(5,1),aligned_edge=UP+LEFT),
        )
        ext_array = np.uint8(
            [[(255,0,0,(x+y>255)*(x+y)) for x in range(0, 256)] for y in range(0, 256)]
        )
        extdev=Group(
            ImageMobject(ext_array[:,-1::-1]).stretch_to_fit_width(2).stretch_to_fit_height(1).move_to(ax.coords_to_point(1,0),aligned_edge=DOWN+LEFT),
        )
        smalldev.z_index=-1
        largedev.z_index=-1
        moddev.z_index=-1
        extdev.z_index=-1

        self.play(FadeIn(smalldev))
        self.slide_break()
        self.play(FadeIn(largedev))
        self.slide_break()
        self.play(FadeIn(moddev))
        self.slide_break()
        self.play(FadeIn(extdev))
        self.slide_break()

        zero_err=MyMathTex(r"Z=\min_\alpha \frac{\Dm_\alpha\reli{1}}{\Dm_\alpha\reli{2}}").scale(0.75).move_to(rel_ent).scale(0.75).shift(4*LEFT)
        self.play(Write(zero_err))
        self.slide_break()

        sigmoid=Group(ax,l,th,rel_ent,zero_err,axis_labels,smalldev,moddev,largedev,extdev)
        self.play(sigmoid.animate.scale(0.625).shift(3*LEFT+UP))
        self.slide_break()

        tab = MobjectTable(
            [
                [MyTex("Zero"), MyMathTex(r"Z")],
                [MyTex("Exp small"), MyMathTex(r"(Z,C)")],
                [MyTex("Subexp small"), MyMathTex(r"C-\omega(1/\sqrt n)\cap o(1)")],
                [MyTex(r"Const ($<0.5$)"), MyMathTex(r"C- \Theta(1/\sqrt n)")],
                [MyTex(r"Const ($>0.5$)"), MyMathTex(r"C+ \Theta(1/\sqrt n)")],
                [MyTex("Subexp large"), MyMathTex(r"C+\omega(1/\sqrt n)\cap o(1)")],
                [MyTex("Exp large"), MyMathTex(r"(C,\infty)")],
                [MyTex("Superexp large"), MyMathTex(r"\infty")],
            ],
            row_labels=[
                MyTex("Zero err"),
                MyTex("Lrg$_<$"),
                MyTex("Mod$_<$"),
                MyTex("Sml$_<$"),
                MyTex("Sml$_>$"),
                MyTex("Mod$_>$"),
                MyTex("Lrg$_>$"),
                MyTex("Ext")
            ],
            col_labels=[MyMathTex(r"\epsilon_n"), MyMathTex(r"R_n")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
            v_buff=0.5,
        ).scale(0.4).shift(3.5*RIGHT+UP)

        tab[1].set(stroke_width=2)
        # tab[4].set(stroke_width=2)
        tab[8].set(stroke_width=2)
        tab[0][8+3:14+3].set_color(BLUE)
        tab[0][5+3:8+3].set_color(GREEN)
        tab[0][14+3:17+3].set_color(GREEN)
        tab[0][2+3:5+3].set_color(YELLOW)
        tab[0][17+3:20+3].set_color(YELLOW)
        tab[0][20+3:].set_color(RED)
        tab[0][2:5].set_color(RED)

        self.play(Write(tab[1]),Write(tab[5]),Write(tab[9]))
        self.play(FadeIn(tab[0][0:2]))
        self.play(*[FadeIn(tab[0][2+3*i]) for i in range(8)])
        self.slide_break()

        self.play(FadeIn(tab[0][9+3:11+3]),FadeIn(tab[0][12+3:14+3]))
        self.slide_break()
        eqn=MyMathTex(r"R_n(\epsilon)\simeq\frac{D\reli{1}}{D\reli{2}}+\sqrt{\frac{D\reli{1}V\reli{2}}{nD\reli{2}}}\cdot S_\nu^{-1}(\epsilon)",color=BLUE,scale=0.75).move_to(2.5*DOWN)
        self.play(Write(eqn))
        self.slide_break()

        self.play(FadeOut(eqn),FadeIn(tab[0][3+3:5+3]),FadeIn(tab[0][18+3:20+3]))
        eqn=MyMathTex(r"R_n\left(1-e^{-\lambda n}\right)\simeq\inf_{\substack{t_1>1\\t_2\in(0,1)}}\frac{\Dm_{t_1}\reli{1}+\left(\frac{t_2}{1-t_2}-\frac{t_1}{t_1-1}\right)\lambda}{\Dm_{t_2}\reli{2}}",color=YELLOW,scale=0.75).move_to(2.5*DOWN)
        self.play(Write(eqn))
        self.slide_break()

        self.play(FadeOut(eqn),FadeIn(tab[0][6+3:8+3]),FadeIn(tab[0][15+3:17+3]))
        eqn=MyMathTex(
            r"R_n\left(e^{-\lambda n^a}\right)&=\frac{D\reli{1}-\left|1-\nu^{-1/2}\right|\sqrt{2V\reli{1}\cdot\lambda n^{a-1}}}{D\reli{2}}\\"
            r"R_n\left(1-e^{-\lambda n^a}\right)&=\frac{D\reli{1}+\left[1+\nu^{-1/2}\right]\sqrt{2V\reli{1}\cdot\lambda n^{a-1}}}{D\reli{2}}\\"
            ,color=GREEN,scale=0.75).move_to(2.5*DOWN)
        self.play(Write(eqn))
        self.slide_break()

        self.play(FadeOut(eqn),FadeIn(tab[0][3:5]),FadeIn(tab[0][21+3:]))
        eqn=MyMathTex(r"R_n\left(0\right)\stackrel{\text{ev.}}=\inf_{t\in \overline{\mathbb R}} \frac{\Dm_t\reli{1}}{\Dm_t\reli{2}}",color=RED,scale=0.75).move_to(2.5*DOWN)
        self.play(Write(eqn))
        self.slide_break()

        self.play(FadeOut(sigmoid),FadeOut(tab[0:2]),FadeOut(tab[5]),FadeOut(tab[9]))
        self.slide_break()

        eqn_lrg=MyMathTex(
            r"R_n(e^{-\lambda n})",
            r"""\simeq\inf_{-\lambda < \mu<\lambda}\begin{dcases}
            \sup_{t_2<0}\inf_{t_1<0}\frac{-\Dm_{t_1}\reli{1}+\left( \frac{t_1}{t_1-1}-\frac{t_2}{t_2-1}\right)\mu}{-\Dm_{t_2}\reli{2}} & \mu\leq -D\rel{\sigma_1}{\rho_1}\\
            \inf_{0<t_2<0}\sup_{0<t_1<0}\frac{\Dp_{t_1}\reli{1}+\left( \frac{t_1}{1-t_1}-\frac{t_2}{1-t_2}\right)\mu}{\Dp_{t_2}\reli{2}} & -D\rel{\sigma_1}{\rho_1}\leq \mu\leq 0\\
            \sup_{t_2>1}\inf_{t_1>1}\frac{\Dm_{t_1}\reli{1}+\left( \frac{t_1}{t_1-1}-\frac{t_2}{t_2-1}\right)\mu}{\Dm_{t_2}\reli{2}} & \mu\geq 0
            \end{dcases}""",
            color=YELLOW,scale=0.625).move_to(0.5*UP)
        self.play(Write(eqn_lrg))
        self.slide_break()

        eqn_lrg_old=eqn_lrg
        eqn_lrg=MyMathTex(
            r"\lim_{\lambda\to\infty}",
            r"R_n(e^{-\lambda n})",
            r"\gtrsim\inf_{t\in\overline{\mathbb R}}\frac{\DL_t\reli{1}}{\Dm_t\reli{2}}",
            color=YELLOW,scale=0.625).move_to(0.5*UP)
        self.play(
            FadeIn(eqn_lrg[0]),
            ReplacementTransform(eqn_lrg_old[0:],eqn_lrg[1:])
        )
        self.slide_break()
        self.remove(*eqn_lrg)
        # self.remove(eqn_lrg_old)

        eqn_lrg=MyMathTex(
            r"\lim_{\lambda\to\infty}R_n(e^{-\lambda n})\gtrsim",
            r" ",
            r"\inf_{t\in\overline{\mathbb R}}\frac{\DL_t\reli{1}}{\Dm_t\reli{2}}",
            r" ",
            color=YELLOW,scale=0.625).move_to(0.5*UP)
        eqn_lrg_new=MyMathTex(
            r"\lim_{\lambda\to\infty}R_n(e^{-\lambda n})\gtrsim",
            r"\max\Biggl\lbrace ",
            r"\inf_{t\in\overline{\mathbb R}}\frac{\DL_t\reli{1}}{\Dm_t\reli{2}}",
            r",\inf_{t\in\overline{\mathbb R}}\frac{\DL_t^*\reli{1}}{\Dm_t\reli{2}} \Biggr\rbrace",
            color=YELLOW,scale=0.625).move_to(0.5*UP)
        self.play(Transform(eqn_lrg,eqn_lrg_new))
        self.slide_break()
        self.remove(*eqn_lrg)

        eqn_lrg_old=MyMathTex(
            r"\lim_{\lambda\to\infty}R_n(e^{-\lambda n})\gtrsim",
            r"\max\Biggl\{",
            r"\inf_{t\in\overline{\mathbb R}}{",
            r"\DL_t\reli{1}",
            r" ",
            r"\over \Dm_t\reli{2}}",
            r",\inf_{t\in\overline{\mathbb R}}{",
            r"\DL_t^*\reli{1}",
            r"\over \Dm_t\reli{2}}",
            r"\Biggr\}",
            color=YELLOW,scale=0.625).move_to(0.5*UP)
        eqn_lrg=MyMathTex(
            r"\lim_{\lambda\to\infty}R_n(e^{-\lambda n})\gtrsim",
            r"\inf_{t\in\overline{\mathbb R}}{",
            r"\max\Bigl\{ ",
            r"\DL_t\reli{1}",
            r",",
            r"\DL_t^*\reli{1}",
            r"\Bigr\}",
            r"\over \Dm_t\reli{2}}",
            color=YELLOW,scale=0.625).move_to(0.5*UP)
        self.play(
            ReplacementTransform(eqn_lrg_old[0],eqn_lrg[0]),
            ReplacementTransform(eqn_lrg_old[1],eqn_lrg[2]),
            ReplacementTransform(eqn_lrg_old[2],eqn_lrg[1]),
            ReplacementTransform(eqn_lrg_old[3],eqn_lrg[3]),
            ReplacementTransform(eqn_lrg_old[4],eqn_lrg[4]),
            ReplacementTransform(eqn_lrg_old[5],eqn_lrg[7]),
            FadeOut(eqn_lrg_old[6]),
            ReplacementTransform(eqn_lrg_old[7],eqn_lrg[5]),
            ReplacementTransform(eqn_lrg_old[8],eqn_lrg[7]),
            ReplacementTransform(eqn_lrg_old[9],eqn_lrg[6]),
        )
        self.slide_break()
        self.remove(*eqn_lrg)
        # self.remove(*eqn_lrg_old)

        eqn_lrg_old=MyMathTex(
            r"\lim_{\lambda\to\infty}R_n(e^{-\lambda n})\gtrsim\inf_{t\in\overline{\mathbb R}}{",
            r"\max\Bigl\{\DL_t\reli{1},\DL_t^*\reli{1}\Bigr\}",
            r"\over \Dm_t\reli{2}}",
            color=YELLOW,scale=0.625).move_to(0.5*UP)
        eqn_lrg=MyMathTex(
            r"\lim_{\lambda\to\infty}R_n(e^{-\lambda n})\gtrsim\inf_{t\in\overline{\mathbb R}}{",
            r"\Dm_t\reli{1}",
            r"\over \Dm_t\reli{2}}",
            color=YELLOW,scale=0.625).move_to(0.5*UP)
        self.play(ReplacementTransform(eqn_lrg_old,eqn_lrg))
        self.slide_break()

        self.play(FadeOut(eqn_lrg))
        self.slide_break()

        order=MyMathTex(
            r"\Dm_t\reli{1}&>\Dm_t\reli{2}~\forall t & &\implies & \left(\rho_1,\sigma_1\right)\succeq \left(\rho_2,\sigma_2\right)\\",
            r"\Dm_t\reli{1}&\geq \Dm_t\reli{2}~\forall t & &\impliedby & \left(\rho_1,\sigma_1\right)\succeq \left(\rho_2,\sigma_2\right)\\",
            color=RED,
            scale=0.75,
        )
        self.play(Write(order))
        self.slide_break()

        self.play(FadeOut(order),FadeOut(eqn))
        self.slide_break()

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), Restore(heading))
        if heading_prev:
            self.slide_break()
            heading_next = toc[tocindex+1].copy().move_to(ORIGIN).scale(1.5).to_corner(UP)
            self.remove(toc[tocindex+1])
            self.play(FadeOut(toc[:tocindex]),FadeOut(heading),FadeOut(toc[tocindex+2:]), TransformFromCopy(toc[tocindex+1],heading_next))
            self.wait()

class Conclusion(SlideScene):
    def construct(self):
        tocindex = 4
        heading = toc[tocindex].copy()
        heading.save_state()
        if heading_prev:
            heading.move_to(ORIGIN).scale(1.5).to_corner(UP)
            self.add(heading,footer)
        else:
            self.add(toc[:tocindex],toc[tocindex+1:],footer)
            self.play(FadeOut(toc[:tocindex]),FadeOut(toc[tocindex+1:]),heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{marvosym} \usepackage{fontawesome}")

        summary1=VGroup(
            MyTex(r"\textbullet Optimal second-order rates"),
            MyTex(r"\textbullet All error regimes"),
            MyTex(r"\textbullet Even zero-error"),
            MyTex(r"\textbullet Cleaner proofs"),
        ).set_color(BLUE).arrange(DOWN,aligned_edge=LEFT).scale(0.8).shift(3.5*LEFT+1*UP)

        summary2=VGroup(
            MyTex(r"\textbullet Operational interpretations"),
            MyTex(r"\textbullet Resource resonance (weak+strong)"),
            MyTex(r"\textbullet New entropy"),
            MyTex(r"\textbullet Two-sided errors"),
        ).set_color(RED).arrange(DOWN,aligned_edge=LEFT).scale(0.8).shift(3.5*RIGHT+1*UP)

        for s in summary1:
            self.play(Write(s))
            self.slide_break()

        for s in summary2:
            self.play(Write(s))
            self.slide_break()

        arxiv=MyTex(r"\texttt{\bfseries arXiv:~" + arxivnum + r"}").scale(1.5).shift(1*DOWN).scale(1)
        thanks=MyTex("Thanks!").shift(2*DOWN).scale(1.5).set_color(YELLOW)
        self.play(Write(arxiv))
        self.remove(footer)
        concfooter=footer.copy()
        self.add(concfooter)
        footer_big=concfooter.copy().arrange(RIGHT,buff=.375).to_corner(DOWN).shift(0.25*UP).scale(1.25).set_opacity(1)
        self.play(Transform(concfooter,footer_big))
        self.play(Write(thanks))

        self.slide_break()
