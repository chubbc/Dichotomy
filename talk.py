from manim_slide import *
import math

config.background_color = "#161c20"
reponame = "Dichotomy"
arxivnum = "2303.05524"

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
        # title = MyTex(r"\bfseries\textsc{Quantum dichotomies and coherent\\thermodynamics beyond first-order asymptotics}").scale(1.25).shift(2.5*UP)
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
        self.slide_break()
        self.play(Unwrite(VGroup(title,arxiv,name,ethz,collab)))
        self.play(ReplacementTransform(footer_big,footer))
        self.slide_break()

        mt=MyTex(r"Infomation\\theory").set_color(RED).shift(4*LEFT+2*DOWN)
        cc=MyTex(r"Quantum\\dichotomies").shift(1*DOWN)
        kk=MyTex(r"Quantum\\thermodynamics").set_color(BLUE).shift(4*RIGHT+2*DOWN)
        arrow=CurvedArrow(start_point=4*LEFT,end_point=4*RIGHT,angle=-PI/3).shift(1.25*DOWN)
        arrow[0].set_color([BLUE,WHITE,RED]).set_sheen_direction(LEFT)
        arrow[1].set_color(BLUE)
        Group(mt,cc,kk,arrow).shift(2*UP)

        mt_pic=Group(
            ImageMobject("mt.jpg").set_height(1.5),
            ImageMobject("jr.jpg").set_height(1.5),
        ).arrange(RIGHT,buff=0).move_to(4*LEFT+1.5*DOWN)
        cc_pic=ImageMobject("cc.jpg").set_height(2).shift(1*DOWN)
        kk_pic=Group(
            ImageMobject("kk.jpg").set_height(1.5),
            ImageMobject("plb.jpg").set_height(1.5),
        ).arrange(RIGHT,buff=0).move_to(4*RIGHT+1.5*DOWN)

        self.play(Write(kk))
        self.slide_break()
        self.play(Write(mt))
        self.slide_break()
        self.play(Write(arrow))
        self.play(Write(cc))
        self.slide_break()

        self.play(FadeIn(mt_pic))
        self.play(FadeIn(kk_pic))
        self.play(FadeIn(cc_pic))
        self.slide_break()

        self.play(FadeOut(*[cc,kk,mt,mt_pic,kk_pic,cc_pic,arrow]))
        self.slide_break()

        self.play(FadeIn(toc))
        self.slide_break()

        self.play(toc[0].animate.scale(1.2).set_color(YELLOW))
        self.slide_break()

        for i in range(1,len(toc)):
           self.play(toc[i].animate.scale(1.2).set_color(YELLOW),toc[i-1].animate.scale(1/1.2).set_color(WHITE))
           self.slide_break()

        self.play(toc[-1].animate.scale(1/1.2).set_color(WHITE))

class Results(SlideScene):
    def construct(self):
        tocindex = 0
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
        self.slide_break()

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
                MyMathTex(r"\left| \phi\right\rangle \xrightarrow{\text{LOCC}} \left| \psi\right\rangle  \quad\iff\quad (\mathrm{Tr}_2|\phi\rangle\langle\phi|,|0\rangle\langle 0|)\prec (\mathrm{Tr}_2|\psi\rangle\langle\psi|,|0\rangle\langle 0|)"),
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
                \end{dcases}""",
            ).scale(0.75)
            for i in range(4):
                self.play(FadeIn(notation[2*i:2*i+2]))
                self.slide_break()
            self.play(FadeOut(notation))
            self.slide_break()

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class HT(SlideScene):
    def construct(self):
        tocindex = 1
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
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
            ).scale(0.5).shift(DOWN)
            axis_labels=axes.get_axis_labels(x_label=r"\alpha",y_label=r"\beta")

            self.play(FadeIn(axes),FadeIn(axis_labels))
            self.slide_break()

            x=np.array([])
            y=np.array([])
            for i in range(1000):
                xx=0.0
                yy=0.0
                while (xx+1)*(yy+1)<=2:
                    xx=np.random.rand()
                    yy=np.random.rand()
                x=np.append(x,xx)
                y=np.append(y,yy)

            pts=VGroup(*[
                Circle(0.02,color=BLUE,fill_opacity=1).move_to(axes.coords_to_point(x[i],y[i])) for i in range(1000)
            ])
            self.play(Write(pts[0]))
            self.slide_break()
            self.play(Write(pts[1]),run_time=1)
            self.play(Write(pts[2]),run_time=1/2)
            self.play(Write(pts[3]),run_time=1/4)
            self.play(Write(pts[4]),run_time=1/8)
            self.play(Write(pts[5]),run_time=1/16)
            self.play(Write(pts[6]),run_time=1/32)
            self.play(Write(pts[7]),run_time=1/64)
            self.play(Write(pts[8]),run_time=1/128)
            self.play(Write(pts[9:]))
            X=[i/100 for i in range(101)]
            Y=[2/(i/100+1)-1 for i in range(101)]

            lorenz=axes.plot_line_graph(
                x_values = X,
                y_values = Y,
                vertex_dot_radius=0,
                # line_color=GRAY,
                line_color=BLUE,
                stroke_width = 3,
            )
            self.play(FadeOut(pts),FadeIn(lorenz))
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
            self.play(sigmoid.animate.scale(0.625).shift(3*LEFT))
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
            ).scale(0.5).shift(3.5*RIGHT)

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
            self.play(FadeIn(tab[0][6:8]),FadeIn(tab[0][15:17]))
            self.slide_break()
            self.play(FadeIn(tab[0][3:5]),FadeIn(tab[0][18:20]))
            self.slide_break()
            self.play(FadeIn(tab[0][21:]))
            self.slide_break()

            self.play(FadeOut(sigmoid),FadeOut(tab[0:2]),FadeOut(tab[4]),FadeOut(tab[8]))
            self.slide_break()

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))


class Reduction(SlideScene):
    def construct(self):
        tocindex = 2
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
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

            newdpi=MyMathTex(r"\beta_x",r"(\rho_1",r"\|",r"\sigma_1)",r"\geq ",r"\beta_x",r"(\rho_2",r"\|",r"\sigma_2)")
            newdpi[:4].set_color(BLUE)
            newdpi[5:].set_color(RED)
            newdpi.shift(dpi[4].get_center()-newdpi[4].get_center())
            self.play(Transform(dpi,newdpi))
            self.slide_break()

            olddpi=dpi
            dpi=MyMathTex(r"\beta_x",r"(\rho_1",r"\|",r"\sigma_1)",r"\geq ",r"\beta_x",r"(\rho_2",r"\|",r"\sigma_2)",r"~~\forall x")
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
            newdpi=MyMathTex(r"\beta_x",r"(\rho_1",r"\|",r"\sigma_1)",r"\geq ",r"\beta_{x-\epsilon_\rho}",r"(\rho_2",r"\|",r"\sigma_2)+\epsilon_\sigma",r"~~\forall x").shift(DOWN)
            newdpi[:4].set_color(BLUE)
            newdpi[5:-1].set_color(RED)
            # oldiff=iff
            newiff=MyMathTex(r"\implies").rotate(-PI/2)
            self.play(Transform(when,newwhen),Transform(dpi,newdpi),Transform(iff,newiff))
            self.slide_break()

            self.play(FadeOut(iff),FadeOut(when),dpi.animate.shift(2*DOWN))
            self.slide_break()

            X=np.linspace(0,1,101)
            Y1=[1.0, 0.9707698741125, 0.9429692026125, 0.9164492003125, 0.8910892735125, 0.86678119605, 0.8434492378125, 0.821000125, 0.79937844805, 0.7785107525124999, 0.7583597362, 0.7388696846125, 0.72, 0.7017115405125001, 0.68397928005, 0.6667601122, 0.6500311751125001, 0.6337703266125, 0.6179500253125, 0.6025496878125, 0.5875493753125001, 0.5729297731125, 0.5586780177999999, 0.5447700191125, 0.5311996800000001, 0.5179496503125001, 0.5050087375125, 0.4923604962, 0.48, 0.46791149601250004, 0.4560905110125, 0.4445219538, 0.43320178, 0.4221207618, 0.4112699266125, 0.4006405512, 0.3902292316125, 0.3800275751125, 0.37002245005, 0.36022085605, 0.35060992151250003, 0.34118202405, 0.33193932045, 0.3228696046125, 0.3139704451125, 0.3052394322, 0.2966695861125, 0.28825867844999997, 0.28, 0.2718914965125, 0.2639311306125, 0.2561125165125, 0.2484381042, 0.24089735125, 0.23348854751250003, 0.22620999551249998, 0.21906001045, 0.2120328151125, 0.2051309396125, 0.19834871531249998, 0.19168065280000002, 0.18512931461249998, 0.17868931451250003, 0.1723592962, 0.16613791244999998, 0.16002005004999997, 0.1540082350125, 0.14809745124999996, 0.1422828498, 0.1365705956125, 0.13095223781249998, 0.12543026061249996, 0.12, 0.11466041444999997, 0.10941046851250003, 0.10424913281249998, 0.09917203611250003, 0.09418158404999999, 0.08927676480000002, 0.0844501003125, 0.07970721051250002, 0.07504077520000002, 0.07045315031249999, 0.06594655031250002, 0.06151083501249999, 0.057151390312499994, 0.05286735461250003, 0.04865197781249997, 0.044510442512500026, 0.04043902420000001, 0.03643698420000002, 0.03250078125, 0.028632559612499997, 0.024831591112499996, 0.02109715125, 0.01742318205000004, 0.013817074049999989, 0.010270209112499984, 0.006787213012500015, 0.0033623112000000233, 0.0]
            Y2=[1.0, 0.9164297434195385, 0.8542295386492529, 0.8055693359683184, 0.7658409898581401, 0.7323804085581163, 0.7035288729353733, 0.6781993433459725, 0.6556588648009719, 0.6353705942706472, 0.616950535113686, 0.6000989322988552, 0.5845785570878573, 0.5702017654011259, 0.5568304808071024, 0.5443319455913493, 0.5326107677880413, 0.5215786111240267, 0.5111587991879741, 0.5012900977223615, 0.4919202815987757, 0.48300060598742645, 0.4744901261882408, 0.46635049842564946, 0.4585501397035447, 0.45105933614227756, 0.44385012229798093, 0.43690021648078237, 0.43018851636520783, 0.42369112618881327, 0.4173969544251598, 0.41128025926079315, 0.405331506646209, 0.39953784220231614, 0.3938797891267132, 0.38834939934635937, 0.3829320014882662, 0.37762042556862063, 0.3724009117865028, 0.36726696807981735, 0.3622022695043901, 0.35720762183187227, 0.35226732339229877, 0.3473726705144645, 0.34252169640284286, 0.3377027865396897, 0.33291104685666684, 0.3281384936861852, 0.32337730574783496, 0.3186198020161595, 0.3138616456557691, 0.3090986183209299, 0.30432015522859673, 0.29952224149210627, 0.29470097652526395, 0.2898493093971859, 0.2849602537822296, 0.2800301872993765, 0.2750522820984049, 0.27002311289224734, 0.26493939498824615, 0.2597911726843748, 0.254578745225316, 0.24929227728310294, 0.24393237367644555, 0.2384928777643932, 0.2329712735432185, 0.22736164883614884, 0.22166182419452696, 0.2158698654671785, 0.20998037664944913, 0.20399185299981099, 0.19790308931422174, 0.19171704265573974, 0.18542163823278007, 0.17902821630997373, 0.17252916585443656, 0.1659289557578949, 0.159228587281818, 0.1524294923015767, 0.14553764556039617, 0.13855135098040255, 0.1314817269789122, 0.12433222277090716, 0.11711095718282777, 0.10982237448101922, 0.10247985758209566, 0.09508883961696113, 0.08765942729784615, 0.08020215184591717, 0.07273219655256707, 0.06526078496506149, 0.05779937781237249, 0.0503596096729127, 0.0429574696661571, 0.03560045640053261, 0.028308720238568952, 0.02108955941169416, 0.01395847049557386, 0.0069223217505272605, 0.0]

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
                    x_values = X[5*i:5*i+4],
                    y_values = Y2[5*i:5*i+4],
                    vertex_dot_radius=0,
                    line_color=RED,
                    stroke_width = 3,
                ) for i in range(20)
            ])

            self.play(Write(ax))
            self.play(Write(lc1),Write(lc2))
            self.add(lcd)
            self.slide_break()

            #x=round(25*(lc2['vertex_dots'][0].get_x()-lcd[0]['vertex_dots'][0].get_x()))
            x=0
            y=0
            while any([Y2[i]+y/100<Y1[i+x] for i in range(101-x)]):
                y+=1
            self.play(lc2.animate.shift((x/25)*RIGHT+(y/25)*UP))
            self.slide_break()

            brace_v=BraceBetweenPoints(ax.coords_to_point(1,0),ax.coords_to_point(1,y/100)).set_color(YELLOW)
            brace_v_lab=MyMathTex(r"\epsilon_\sigma").set_color(YELLOW).scale(0.75).next_to(brace_v,buff=0.1)
            brace_v_lab.add_updater(lambda mobject: mobject.next_to(brace_v,buff=0.1))

            self.play(Write(brace_v))
            self.play(FadeIn(brace_v_lab))
            self.slide_break()

            (x_old,y_old)=(x,y)
            (x,y)=(2,0)
            while any([Y2[i]+y/100<Y1[i+x] for i in range(101-x)]):
                y+=1
            self.play(
                lc2.animate.shift(((x-x_old)/25)*RIGHT+((y-y_old)/25)*UP),
                Transform(brace_v,BraceBetweenPoints(ax.coords_to_point(1,0),ax.coords_to_point(1,y/100)).set_color(YELLOW)),
            )
            self.slide_break()

            brace_h=BraceBetweenPoints(ax.coords_to_point(x/100,1),ax.coords_to_point(0,1)).set_color(YELLOW)
            brace_h_lab=MyMathTex(r"\epsilon_\rho").set_color(YELLOW).scale(0.75).next_to(brace_h,UP,buff=0.1)
            brace_h_lab.add_updater(lambda mobject: mobject.next_to(brace_h,UP,buff=0.1))
            self.play(Write(brace_h))
            self.play(FadeIn(brace_h_lab))
            self.slide_break()

            (x_old,y_old)=(x,y)
            (x,y)=(4,0)
            while any([Y2[i]+y/100<Y1[i+x] for i in range(101-x)]):
                y+=1
            self.play(
                lc2.animate.shift(((x-x_old)/25)*RIGHT+((y-y_old)/25)*UP),
                Transform(brace_v,BraceBetweenPoints(ax.coords_to_point(1,0),ax.coords_to_point(1,y/100)).set_color(YELLOW)),
                Transform(brace_h,BraceBetweenPoints(ax.coords_to_point(x/100,1),ax.coords_to_point(0,1)).set_color(YELLOW)),
            )
            self.slide_break()

            brace_h_lab.clear_updaters()
            brace_h_lab.clear_updaters()

            self.play(VGroup(ax,lc1,lc2,lcd,brace_h,brace_v,brace_h_lab,brace_v_lab).animate.shift(3*LEFT))
            ax_err=Axes(
                x_range=[0,.2,.2],
                y_range=[0,.2,.2],
                x_length=8,
                y_length=8,
            ).scale(0.5).shift(3*RIGHT).set_color(YELLOW)
            self.play(Write(ax_err))
            self.slide_break()

            err_labs=VGroup(
                MyMathTex(r"\epsilon_\rho").scale(1).move_to(ax_err.coords_to_point(0.1,-0.02)),
                MyMathTex(r"\epsilon_\sigma").scale(1).rotate(PI/2).move_to(ax_err.coords_to_point(-0.02,0.1)),
            ).set_color(YELLOW)
            self.play(
                ReplacementTransform(VGroup(brace_h,brace_h_lab),err_labs[0]),
                ReplacementTransform(VGroup(brace_v,brace_v_lab),err_labs[1]),
            )

            err_pts=VGroup()
            err_pts+=Circle(radius=0.05,color=YELLOW,fill_opacity=1).move_to(ax_err.coords_to_point(x/100,y/100))
            self.play(Flash(err_pts[-1]),FadeIn(err_pts[-1]))
            self.slide_break()

            for t in range(4,6):
                (x_old,y_old)=(x,y)
                (x,y)=(t,-100)
                while any([Y2[i]+y/100<Y1[i+x] for i in range(101-x)]):
                    y+=1
                self.play(
                    lc2.animate.shift(((x-x_old)/25)*RIGHT+((y-y_old)/25)*UP),
                    run_time=0.1
                )
            err_pts+=Circle(radius=0.05,color=YELLOW,fill_opacity=1).move_to(ax_err.coords_to_point(x/100,y/100))
            self.play(Flash(err_pts[-1]),FadeIn(err_pts[-1]))
            self.slide_break()

            for t in range(6,8):
                (x_old,y_old)=(x,y)
                (x,y)=(t,-100)
                while any([Y2[i]+y/100<Y1[i+x] for i in range(101-x)]):
                    y+=1
                self.play(
                    lc2.animate.shift(((x-x_old)/25)*RIGHT+((y-y_old)/25)*UP),
                    run_time=0.1
                )
            err_pts+=Circle(radius=0.05,color=YELLOW,fill_opacity=1).move_to(ax_err.coords_to_point(x/100,y/100))
            self.play(Flash(err_pts[-1]),FadeIn(err_pts[-1]))
            self.slide_break()

            xx=[i for i in range(10)]
            yy=[i for i in range(10)]
            for i in range(10):
                yy[i]=-10
                while any([Y2[j]+yy[i]/100<Y1[j+xx[i]] for j in range(101-xx[i])]):
                    yy[i]+=1
            # print(xx)
            # print(yy)
            yy[-1]=0
            err_line=ax_err.plot_line_graph(
                x_values = [xxx/100 for xxx in xx],
                y_values = [yyy/100 for yyy in yy],
                vertex_dot_radius=0,
                line_color=YELLOW,
                stroke_width = 2,
            )
            # self.add(err_line)
            self.play(FadeIn(err_line),FadeOut(err_pts))
            self.slide_break()

            self.play(
                FadeOut(VGroup(ax,lc1,lc2,lcd)),
                FadeOut(ax_err),
                FadeOut(err_line),
                FadeOut(err_labs),
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

            pinch_meme=ImageMobject("pinch_meme.jpg").set_height(4).shift(DOWN)
            self.play(whatif.animate.shift(2*UP))
            self.play(FadeIn(pinch_meme))
            self.slide_break()

            self.play(FadeOut(pinch_meme))
            self.slide_break()

            pinch=VGroup()
            pinch+=MyMathTex(r"\beta_x\reli{1}",r"\geq ",r"\beta_{x-\epsilon_\rho}\reli{2}",r"~~\forall x")
            pinch[-1][0].set_color(BLUE)
            pinch[-1][2].set_color(RED)
            pinch+=MyMathTex(r"\impliedby").rotate(-PI/2)
            pinch+=MyMathTex(r"(\rho_1,\sigma_1)",r"\succeq_{(\epsilon_\rho,\epsilon_\sigma)} ",r"(\rho_2,\sigma_2)")
            pinch[-1][0].set_color(BLUE)
            pinch[-1][2].set_color(RED)
            pinch+=MyMathTex(r"\impliedby").rotate(-PI/2)
            pinch+=MyMathTex(r"\beta_x\rel{\mathcal P_{\sigma_1}(\rho_1)}{\sigma_1}",r"\geq ",r"\beta_{x-\epsilon_\rho}\reli{2}",r"~~\forall x")
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

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class Rates(SlideScene):
    def construct(self):
        tocindex = 3
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
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
        self.play(sigmoid.animate.scale(0.625).shift(3*LEFT))
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
        ).scale(0.5).shift(3.5*RIGHT)

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
        self.play(FadeIn(tab[0][6+3:8+3]),FadeIn(tab[0][15+3:17+3]))
        self.slide_break()
        self.play(FadeIn(tab[0][3+3:5+3]),FadeIn(tab[0][18+3:20+3]))
        self.slide_break()
        self.play(FadeIn(tab[0][3:5]),FadeIn(tab[0][21+3:]))
        self.slide_break()

        self.play(FadeOut(sigmoid),FadeOut(tab[0:2]),FadeOut(tab[5]),FadeOut(tab[9]))
        self.slide_break()

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))


class Conclusion(SlideScene):
    def construct(self):
        tocindex = 4
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
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
            MyTex(r"\textbullet Two-sided error"),
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
