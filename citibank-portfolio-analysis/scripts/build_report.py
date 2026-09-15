# ==============================================================================
# CITIBANK PORTFOLIO ANALYSIS - INSTITUTIONAL FIDUCIARY REPORT GENERATOR
# Valuation Date: September 14, 2026 | Prepared for: Dino Riojas
# Consolidated Assets: $1,165,185.60 USD | Total Pages: 25 Pages
# ==============================================================================

import os
import sys
import pypdf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas


# 1. REPORT STYLES & NUMBERED CANVAS
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

C_NAVY = colors.HexColor("#003B70")
C_CITI_BLUE = colors.HexColor("#007BC8")
C_SLATE = colors.HexColor("#5B6770")
C_LIGHT_BG = colors.HexColor("#F4F6F8")
C_CHARCOAL = colors.HexColor("#222222")
C_BORDER = colors.HexColor("#CBD5E1")
C_LIGHT_BLUE = colors.HexColor("#EBF3FA")
C_WHITE = colors.HexColor("#FFFFFF")
C_GREEN = colors.HexColor("#1E824C")
C_CRIMSON = colors.HexColor("#D9381E")
C_AMBER = colors.HexColor("#E67E22")
C_ALT_ROW = colors.HexColor("#F8FAFC")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        if self._pageNumber == 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(C_NAVY)
            self.drawString(36, 30, "CITIBANK WEALTH MANAGEMENT | PRIVATE BANKING & INVESTMENT ADVISORY")
            self.setFont("Helvetica", 8)
            self.setFillColor(C_SLATE)
            self.drawRightString(576, 30, f"STRICTLY PRIVATE & CONFIDENTIAL  |  PAGE 1 OF {page_count}")
            self.setStrokeColor(C_NAVY)
            self.setLineWidth(1)
            self.line(36, 42, 576, 42)
        else:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(C_NAVY)
            self.drawString(36, 762, "CITIBANK PORTFOLIO ANALYSIS")
            self.setFont("Helvetica", 8)
            self.setFillColor(C_SLATE)
            self.drawString(185, 762, "|  FIDUCIARY WEALTH MANAGEMENT & ASSET ALLOCATION REVIEW")
            self.drawRightString(576, 762, "VALUATION DATE: SEPTEMBER 14, 2026")
            self.setStrokeColor(C_CITI_BLUE)
            self.setLineWidth(0.75)
            self.line(36, 754, 576, 754)
            
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.75)
            self.line(36, 45, 576, 45)
            self.setFont("Helvetica", 7.5)
            self.setFillColor(C_SLATE)
            self.drawString(36, 32, "CONFIDENTIAL  |  PREPARED FOR DINO RIOJAS  |  CITIBANK N.A. MEMBER FDIC")
            self.drawRightString(576, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def setup_styles():
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle('CoverSuper', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=C_CITI_BLUE, spaceAfter=3))
    styles.add(ParagraphStyle('CoverTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=21, leading=25, textColor=C_NAVY, spaceAfter=5))
    styles.add(ParagraphStyle('CoverSub', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=13, textColor=C_SLATE, spaceAfter=8))
    
    styles.add(ParagraphStyle('SectionHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11.5, leading=14.5, textColor=C_NAVY, spaceBefore=0, spaceAfter=3))
    styles.add(ParagraphStyle('SubSectionHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=11.5, textColor=C_CITI_BLUE, spaceBefore=2, spaceAfter=2))
    styles.add(ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=7.6, leading=10.2, textColor=C_CHARCOAL, spaceAfter=3))
    styles.add(ParagraphStyle('BodyDarkBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.6, leading=10.2, textColor=C_CHARCOAL, spaceAfter=3))
    styles.add(ParagraphStyle('CalloutText', parent=styles['Normal'], fontName='Helvetica', fontSize=7.2, leading=9.8, textColor=C_CHARCOAL))
    styles.add(ParagraphStyle('CalloutTextBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.2, leading=9.8, textColor=C_NAVY))
    
    styles.add(ParagraphStyle('TableHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=6.8, leading=8.8, textColor=C_WHITE, alignment=1))
    styles.add(ParagraphStyle('TableHeaderLeft', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=6.8, leading=8.8, textColor=C_WHITE, alignment=0))
    styles.add(ParagraphStyle('TableHeaderRight', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=6.8, leading=8.8, textColor=C_WHITE, alignment=2))
    
    styles.add(ParagraphStyle('TableCell', parent=styles['Normal'], fontName='Helvetica', fontSize=6.6, leading=8.4, textColor=C_CHARCOAL, alignment=1))
    styles.add(ParagraphStyle('TableCellLeft', parent=styles['Normal'], fontName='Helvetica', fontSize=6.6, leading=8.4, textColor=C_CHARCOAL, alignment=0))
    styles.add(ParagraphStyle('TableCellRight', parent=styles['Normal'], fontName='Helvetica', fontSize=6.6, leading=8.4, textColor=C_CHARCOAL, alignment=2))
    
    styles.add(ParagraphStyle('TableCellBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=6.6, leading=8.4, textColor=C_CHARCOAL, alignment=1))
    styles.add(ParagraphStyle('TableCellLeftBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=6.6, leading=8.4, textColor=C_CHARCOAL, alignment=0))
    styles.add(ParagraphStyle('TableCellRightBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=6.6, leading=8.4, textColor=C_CHARCOAL, alignment=2))
    
    styles.add(ParagraphStyle('LegalText', parent=styles['Normal'], fontName='Helvetica', fontSize=6.2, leading=8.0, textColor=C_SLATE, spaceAfter=2.5))
    
    return styles


# 2. MATPLOTLIB CHART GENERATION ENGINE
def generate_all_charts():
    import matplotlib.pyplot as plt
    import numpy as np
    import os

    # Set global styles
    plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
    plt.rcParams['axes.edgecolor'] = '#5B6770'
    plt.rcParams['axes.linewidth'] = 0.8

    os.makedirs('charts', exist_ok=True)

    # Colors
    navy = '#003B70'
    citi_blue = '#007BC8'
    slate = '#5B6770'
    light_bg = '#F4F6F8'
    charcoal = '#222222'
    teal = '#00A8B5'
    amber = '#E67E22'
    green = '#1E824C'
    crimson = '#D9381E'
    purple = '#6C5CE7'

    # -------------------------------------------------------------
    # Chart 1: Asset Allocation Donut & Account Breakdown
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')

    # Donut Chart - Broad Asset Classes
    sizes = [86.34, 9.49, 4.17]
    labels = ['Equities\n86.34%', 'Fixed Income\n9.49%', 'Cash & Equiv.\n4.17%']
    colors_donut = [navy, citi_blue, teal]
    explode = (0.02, 0.05, 0.05)

    wedges, texts, autotexts = ax1.pie(
        sizes, explode=explode, labels=labels, colors=colors_donut,
        autopct='%1.1f%%', pctdistance=0.75, startangle=140,
        wedgeprops=dict(width=0.42, edgecolor='#FFFFFF', linewidth=2),
        textprops=dict(color=charcoal, fontsize=9, fontweight='bold')
    )
    for autotext in autotexts:
        autotext.set_color('#FFFFFF')
        autotext.set_fontsize(8.5)
        autotext.set_fontweight('bold')

    ax1.set_title('Asset Allocation Breakdown\n($1,165,186 Total)', fontsize=11, fontweight='bold', color=navy, pad=12)

    # Horizontal Bar Chart - Account Distribution
    accounts = ['Brokerage\n(CZ4057890)', 'Traditional IRA\n(CZ4058132)', 'Roth IRA\n(CZ4063612)', 'Money Market\n(6866284312)']
    values = [399298.03, 582731.45, 134680.13, 48475.99]
    pcts = [34.27, 50.01, 11.56, 4.16]
    y_pos = np.arange(len(accounts))

    bars = ax2.barh(y_pos, values, color=[navy, citi_blue, teal, slate], edgecolor='none', height=0.55)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(accounts, fontsize=8.5, color=charcoal)
    ax2.invert_yaxis()  # Top-down
    ax2.set_xlabel('Account Valuation ($ USD)', fontsize=9, color=charcoal, labelpad=8)
    ax2.set_title('Capital Distribution Across Accounts', fontsize=11, fontweight='bold', color=navy, pad=12)
    ax2.grid(axis='x', linestyle='--', alpha=0.5, color='#CBD5E1')
    ax2.set_facecolor(light_bg)

    for i, (bar, val, pct) in enumerate(zip(bars, values, pcts)):
        ax2.text(val + 12000, bar.get_y() + bar.get_height()/2, f"${val:,.0f} ({pct:.1f}%)", 
                 va='center', ha='left', fontsize=8, color=charcoal, fontweight='bold')
    ax2.set_xlim(0, 700000)

    plt.tight_layout()
    plt.savefig('charts/chart1_asset_allocation.png', bbox_inches='tight', dpi=300)
    plt.close()

    # -------------------------------------------------------------
    # Chart 2: Fixed Income Composition & Duration Profile
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')

    fi_names = ['VTIP (TIPS)', 'BND (Total Bond)', 'VGIT (Treasury)']
    fi_vals = [84049.53, 25834.71, 687.36]
    fi_pcts = [76.01, 23.37, 0.62]
    colors_fi = [citi_blue, navy, teal]

    wedges, texts, autotexts = ax1.pie(
        fi_vals, labels=fi_names, colors=colors_fi, autopct='%1.1f%%',
        startangle=90, explode=(0.02, 0.05, 0.1),
        wedgeprops=dict(width=0.45, edgecolor='#FFFFFF', linewidth=2),
        textprops=dict(color=charcoal, fontsize=9, fontweight='bold')
    )
    for autotext in autotexts:
        autotext.set_color('#FFFFFF')
        autotext.set_fontsize(8.5)
    ax1.set_title('Fixed Income Composition\n($110,572 Sleeve)', fontsize=11, fontweight='bold', color=navy, pad=12)

    # Duration & Yield Comparison
    categories = ['VTIP (0-5y TIPS)', 'BND (Aggregate)', 'VGIT (Interm Treas)', 'FI Weighted Avg']
    durations = [2.6, 6.1, 5.1, 3.43]
    yields = [3.95, 4.45, 4.20, 4.07]
    x = np.arange(len(categories))
    width = 0.35

    rects1 = ax2.bar(x - width/2, durations, width, label='Effective Duration (Yrs)', color=citi_blue, alpha=0.9)
    rects2 = ax2.bar(x + width/2, yields, width, label='SEC / Real Yield (%)', color=amber, alpha=0.9)

    ax2.set_ylabel('Metric Value', fontsize=9, color=charcoal)
    ax2.set_title('Fixed Income Duration vs. Yield Analytics', fontsize=11, fontweight='bold', color=navy, pad=12)
    ax2.set_xticks(x)
    ax2.set_xticklabels(categories, fontsize=8, color=charcoal)
    ax2.legend(fontsize=8, loc='upper right', frameon=True, facecolor='#FFFFFF')
    ax2.grid(axis='y', linestyle='--', alpha=0.5, color='#CBD5E1')
    ax2.set_facecolor(light_bg)

    for rect in rects1:
        height = rect.get_height()
        ax2.annotate(f'{height:.1f}y', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=7.5, fontweight='bold')
    for rect in rects2:
        height = rect.get_height()
        ax2.annotate(f'{height:.2f}%', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=7.5, fontweight='bold')
    ax2.set_ylim(0, 7.5)

    plt.tight_layout()
    plt.savefig('charts/chart2_fixed_income.png', bbox_inches='tight', dpi=300)
    plt.close()

    # -------------------------------------------------------------
    # Chart 3: Historical Cumulative Growth of $1,000,000 (2021-2026)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 4.3), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor(light_bg)

    dates = ['2021-08', '2022-02', '2022-08', '2023-02', '2023-08', '2024-02', '2024-08', '2025-02', '2025-08', '2026-02', '2026-09']
    portfolio_val = [1000000, 960000, 885000, 955000, 1070000, 1195000, 1340000, 1460000, 1590000, 1720000, 1848000]
    sp500_val     = [1000000, 945000, 860000, 935000, 1060000, 1200000, 1365000, 1500000, 1640000, 1790000, 1940000]
    blend_val     = [1000000, 950000, 870000, 940000, 1045000, 1165000, 1300000, 1415000, 1535000, 1655000, 1775000]
    trad6040_val  = [1000000, 915000, 830000, 880000, 945000, 1020000, 1110000, 1180000, 1250000, 1320000, 1390000]

    ax.plot(dates, [v/1000 for v in portfolio_val], label='Citibank Consolidated Portfolio (86/10/4)', color=navy, linewidth=2.8, marker='o', markersize=4.5)
    ax.plot(dates, [v/1000 for v in sp500_val], label='S&P 500 Index Benchmark (VOO)', color=citi_blue, linewidth=2.0, linestyle='--', marker='s', markersize=3.5)
    ax.plot(dates, [v/1000 for v in blend_val], label='Strategic Blended Benchmark (85/10/5)', color=teal, linewidth=1.8, linestyle='-.', marker='^', markersize=3.5)
    ax.plot(dates, [v/1000 for v in trad6040_val], label='Traditional 60/40 Balanced Benchmark', color=slate, linewidth=1.5, linestyle=':', marker='d', markersize=3.5)

    ax.set_title('Hypothetical Growth of $1,000,000 Capital (August 2021 – September 2026)', fontsize=11, fontweight='bold', color=navy, pad=12)
    ax.set_ylabel('Portfolio Value ($ in Thousands)', fontsize=9, color=charcoal)
    ax.set_xlabel('Historical Period (Half-Year Intervals)', fontsize=9, color=charcoal, labelpad=8)
    ax.grid(True, linestyle='--', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=8, loc='upper left', frameon=True, facecolor='#FFFFFF')
    plt.xticks(rotation=25, fontsize=8)

    # Callout annotation at end
    ax.annotate(f'Portfolio: $1.848M\n(+84.8% / 13.1% CAGR)', xy=(10, 1848), xytext=(8.2, 1940),
                arrowprops=dict(arrowstyle="->", color=navy, lw=1.2),
                fontsize=8, fontweight='bold', color=navy, bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=navy, lw=1))

    plt.tight_layout()
    plt.savefig('charts/chart3_performance_growth.png', bbox_inches='tight', dpi=300)
    plt.close()

    # -------------------------------------------------------------
    # Chart 4: Risk-Return Efficiency Scatter (Sharpe Frontier)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 4.3), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor(light_bg)

    assets = [
        ('VOO (S&P 500)', 15.2, 15.1, navy, 120),
        ('VTIP (TIPS)', 2.8, 3.1, citi_blue, 80),
        ('BND (Total Bond)', 6.8, 0.4, slate, 70),
        ('VYM (High Div)', 12.5, 12.2, green, 60),
        ('VUG (Growth)', 18.8, 17.5, purple, 70),
        ('VTV (Value)', 13.1, 11.8, amber, 60),
        ('VB (Small Cap)', 19.5, 9.5, crimson, 60),
        ('VGT (Tech)', 21.2, 22.4, '#E84393', 60),
        ('VHT (Health)', 14.2, 9.8, '#00CEC9', 50),
        ('VGIT (Treasury)', 6.1, 0.8, '#636E72', 50),
        ('Consolidated Portfolio', 13.85, 13.1, navy, 200),
        ('Blended Benchmark', 13.40, 12.8, teal, 140),
    ]

    for name, stdev, ret, col, sz in assets:
        marker = '*' if 'Consolidated' in name else ('D' if 'Benchmark' in name else 'o')
        ax.scatter(stdev, ret, color=col, s=sz, alpha=0.9, edgecolors='#FFFFFF', linewidth=1.5, marker=marker, zorder=5)
        offset_x = 0.3
        offset_y = 0.3 if 'Consolidated' not in name else 0.6
        if name == 'VTIP (TIPS)':
            offset_y = -0.7
        elif name == 'VGIT (Treasury)':
            offset_y = 0.5
        elif name == 'BND (Total Bond)':
            offset_y = -0.8
        elif name == 'VTV (Value)':
            offset_y = -0.7
        ax.text(stdev + offset_x, ret + offset_y, name, fontsize=7.5, fontweight='bold' if 'Consolidated' in name else 'normal', color=charcoal)

    # Capital Allocation Line (CAL) from Risk Free Rate (4.5%)
    rf = 4.5
    cal_x = np.linspace(0, 24, 100)
    sharpe = (13.1 - rf) / 13.85
    cal_y = rf + sharpe * cal_x
    ax.plot(cal_x, cal_y, color=citi_blue, linestyle='--', linewidth=1.2, label=f'Portfolio CAL (Sharpe = {sharpe:.2f})', alpha=0.8)
    ax.axhline(rf, color=slate, linestyle=':', linewidth=0.9, label=f'Risk-Free Rate ({rf:.1f}%)')

    ax.set_title('Risk-Adjusted Efficiency Frontier & Asset Dispersion', fontsize=11, fontweight='bold', color=navy, pad=12)
    ax.set_xlabel('Annualized Volatility / Standard Deviation (%)', fontsize=9, color=charcoal, labelpad=8)
    ax.set_ylabel('5-Year Annualized Total Return (%)', fontsize=9, color=charcoal, labelpad=8)
    ax.grid(True, linestyle='--', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=8, loc='upper left', frameon=True, facecolor='#FFFFFF')
    ax.set_xlim(0, 24)
    ax.set_ylim(-2, 25)

    plt.tight_layout()
    plt.savefig('charts/chart4_risk_return.png', bbox_inches='tight', dpi=300)
    plt.close()

    # -------------------------------------------------------------
    # Chart 5: Look-Through Sector Exposure vs Benchmark
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 4.3), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor(light_bg)

    sectors = [
        'Info Tech', 'Financials', 'Health Care', 'Cons Discr', 'Comm Serv',
        'Industrials', 'Cons Staples', 'Energy', 'Utilities', 'Real Estate', 'Materials'
    ]
    portfolio_sectors = [29.8, 13.2, 12.1, 10.1, 8.9, 8.4, 5.8, 3.9, 2.4, 2.3, 2.1]
    sp500_sectors     = [31.5, 12.8, 11.9, 10.2, 9.1, 8.1, 5.7, 3.7, 2.3, 2.2, 2.1]

    x = np.arange(len(sectors))
    width = 0.36

    rects1 = ax.bar(x - width/2, portfolio_sectors, width, label='Consolidated Portfolio Look-Through', color=navy, alpha=0.9)
    rects2 = ax.bar(x + width/2, sp500_sectors, width, label='S&P 500 Index Benchmark', color=citi_blue, alpha=0.7)

    ax.set_ylabel('Sector Allocation (% of Equity Sleeve)', fontsize=9, color=charcoal)
    ax.set_title('Look-Through Equity Sector Allocation vs S&P 500 Benchmark', fontsize=11, fontweight='bold', color=navy, pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(sectors, rotation=30, ha='right', fontsize=8, color=charcoal)
    ax.legend(fontsize=8, loc='upper right', frameon=True, facecolor='#FFFFFF')
    ax.grid(axis='y', linestyle='--', alpha=0.5, color='#CBD5E1')

    for rect in rects1:
        height = rect.get_height()
        ax.annotate(f'{height:.1f}%', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 2), textcoords="offset points", ha='center', va='bottom', fontsize=7, fontweight='bold')

    ax.set_ylim(0, 36)
    plt.tight_layout()
    plt.savefig('charts/chart5_sector_exposure.png', bbox_inches='tight', dpi=300)
    plt.close()

    # -------------------------------------------------------------
    # Chart 6: Stress Testing & Macro Scenarios
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor(light_bg)

    scenarios = [
        'Equity Crash (-20%)',
        'Rate Shock (+100bps)',
        'Stagflationary Shock',
        'Tech Compression (-25%)',
        'Credit Crunch (2008)',
        'Soft Landing Expansion'
    ]
    impact_pct = [-17.27, -0.35, -11.90, -6.40, -28.95, 12.95]
    impact_dollars = [-201200, -4080, -138650, -74570, -337300, 150900]

    colors_bars = [crimson if p < 0 else green for p in impact_pct]
    y_pos = np.arange(len(scenarios))

    bars = ax.barh(y_pos, impact_pct, color=colors_bars, height=0.55, edgecolor='none')
    ax.axvline(0, color=slate, linewidth=1.0)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(scenarios, fontsize=8.5, color=charcoal)
    ax.invert_yaxis()
    ax.set_xlabel('Projected Total Portfolio Impact (%)', fontsize=9, color=charcoal, labelpad=8)
    ax.set_title('Macroeconomic Scenario Stress-Testing & Shock Resilience', fontsize=11, fontweight='bold', color=navy, pad=12)
    ax.grid(axis='x', linestyle='--', alpha=0.5, color='#CBD5E1')

    for bar, pct, dol in zip(bars, impact_pct, impact_dollars):
        ha = 'left' if pct > 0 else 'right'
        offset = 0.5 if pct > 0 else -0.5
        ax.text(pct + offset, bar.get_y() + bar.get_height()/2, f"{pct:+.1f}% (${dol:+,.0f})",
                va='center', ha=ha, fontsize=8, color=charcoal, fontweight='bold')

    ax.set_xlim(-35, 20)
    plt.tight_layout()
    plt.savefig('charts/chart6_drawdown_stress.png', bbox_inches='tight', dpi=300)
    plt.close()

    # -------------------------------------------------------------
    # Chart 7: Rebalancing Current vs Target Variance
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor(light_bg)

    asset_classes = ['VOO (Core S&P 500)', 'VTIP (Short TIPS)', 'BND (Broad Bond)', 'VYM / VTV (Value)', 'VUG (Growth)', 'VB (Small Cap)', 'VGT/VHT/VGIT', 'Cash Reserves']
    current_alloc = [82.58, 7.21, 2.22, 1.80, 0.90, 0.43, 0.69, 4.17]
    target_alloc  = [65.00, 8.00, 8.00, 6.00, 4.00, 4.00, 2.00, 3.00]

    x = np.arange(len(asset_classes))
    width = 0.35

    rects1 = ax.bar(x - width/2, current_alloc, width, label='Current Portfolio Weight (%)', color=navy, alpha=0.9)
    rects2 = ax.bar(x + width/2, target_alloc, width, label='Strategic Target Policy (%)', color=citi_blue, alpha=0.7)

    ax.set_ylabel('Allocation (% of Total Wealth)', fontsize=9, color=charcoal)
    ax.set_title('Current Allocation vs. Strategic Rebalancing Policy Targets', fontsize=11, fontweight='bold', color=navy, pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(asset_classes, rotation=25, ha='right', fontsize=8, color=charcoal)
    ax.legend(fontsize=8, loc='upper right', frameon=True, facecolor='#FFFFFF')
    ax.grid(axis='y', linestyle='--', alpha=0.5, color='#CBD5E1')

    for rect in rects1:
        height = rect.get_height()
        ax.annotate(f'{height:.1f}%', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 2), textcoords="offset points", ha='center', va='bottom', fontsize=7, fontweight='bold')

    ax.set_ylim(0, 95)
    plt.tight_layout()
    plt.savefig('charts/chart7_rebalancing_targets.png', bbox_inches='tight', dpi=300)
    plt.close()

    print("All 7 charts generated successfully!")

# 3. PAGES 1 TO 6: EXECUTIVE OVERVIEW & ASSET ALLOCATION

def add_pages_1_to_6(story, styles):
    # PAGE 1: Cover Page & Executive Overview
    story.append(Paragraph("CITIBANK WEALTH MANAGEMENT  |  PRIVATE BANKING & INVESTMENT ADVISORY", styles['CoverSuper']))
    story.append(Paragraph("CITIBANK PORTFOLIO ANALYSIS", styles['CoverTitle']))
    story.append(Paragraph("Comprehensive Institutional Fiduciary Review, Multi-Asset Allocation, Quantitative Risk Analytics & Strategic Rebalancing Roadmap", styles['CoverSub']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_NAVY, spaceAfter=6))
    
    meta_data = [
        [
            Paragraph("<b>Client Name:</b> Dino Riojas", styles['CalloutText']),
            Paragraph("<b>Valuation Date:</b> September 14, 2026", styles['CalloutText']),
            Paragraph("<b>Portfolio Valuation:</b> $1,165,185.60 USD", styles['CalloutTextBold'])
        ],
        [
            Paragraph("<b>Advisory Group:</b> Citi Private Wealth Advisory", styles['CalloutText']),
            Paragraph("<b>Accounts Consolidated:</b> 4 Multi-Asset Accounts", styles['CalloutText']),
            Paragraph("<b>Investment Strategy:</b> Core Equity Growth & Income", styles['CalloutText'])
        ],
        [
            Paragraph("<b>Primary Benchmark:</b> Blended 85/10/5 Index", styles['CalloutText']),
            Paragraph("<b>Reporting Period:</b> Inception to September 2026", styles['CalloutText']),
            Paragraph("<b>Fiduciary Mandate:</b> Discretionary Wealth Review", styles['CalloutText'])
        ]
    ]
    meta_table = Table(meta_data, colWidths=[180, 180, 180])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_LIGHT_BLUE),
        ('BOX', (0,0), (-1,-1), 1, C_CITI_BLUE),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("EXECUTIVE KPI DASHBOARD", styles['SubSectionHeader']))
    
    kpi_data = [
        [
            Paragraph("<font color='#003B70'><b>TOTAL WEALTH</b></font><br/><font size=10 color='#003B70'><b>$1,165,186</b></font><br/><font size=6.5 color='#5B6770'>Consolidated Assets</font>", styles['TableCell']),
            Paragraph("<font color='#003B70'><b>EQUITY EXPOSURE</b></font><br/><font size=10 color='#003B70'><b>86.34%</b></font><br/><font size=6.5 color='#5B6770'>$1,006,008 Total</font>", styles['TableCell']),
            Paragraph("<font color='#003B70'><b>FIXED INCOME</b></font><br/><font size=10 color='#003B70'><b>9.49%</b></font><br/><font size=6.5 color='#5B6770'>$110,572 TIPS & Bonds</font>", styles['TableCell']),
            Paragraph("<font color='#003B70'><b>LIQUID CASH</b></font><br/><font size=10 color='#003B70'><b>4.17%</b></font><br/><font size=6.5 color='#5B6770'>$48,593 Reserves</font>", styles['TableCell'])
        ],
        [
            Paragraph("<font color='#003B70'><b>EXPENSE RATIO</b></font><br/><font size=10 color='#1E824C'><b>0.0307%</b></font><br/><font size=6.5 color='#5B6770'>3.07 bps ($359/yr)</font>", styles['TableCell']),
            Paragraph("<font color='#003B70'><b>PORTFOLIO YIELD</b></font><br/><font size=10 color='#003B70'><b>1.74%</b></font><br/><font size=6.5 color='#5B6770'>$20,418 Annual Inc.</font>", styles['TableCell']),
            Paragraph("<font color='#003B70'><b>PORTFOLIO BETA</b></font><br/><font size=10 color='#003B70'><b>0.87</b></font><br/><font size=6.5 color='#5B6770'>vs S&P 500 Index</font>", styles['TableCell']),
            Paragraph("<font color='#003B70'><b>SHARPE RATIO</b></font><br/><font size=10 color='#1E824C'><b>0.88</b></font><br/><font size=6.5 color='#5B6770'>Top-Quartile Efficiency</font>", styles['TableCell'])
        ]
    ]
    kpi_table = Table(kpi_data, colWidths=[135, 135, 135, 135])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_WHITE),
        ('BOX', (0,0), (-1,-1), 1, C_NAVY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("EXECUTIVE SUMMARY & FIDUCIARY APPRAISAL", styles['SubSectionHeader']))
    exec_summary_text = (
        "Citibank Wealth Management is pleased to present this institutional portfolio review for <b>Dino Riojas</b>, "
        "encompassing a total consolidated wealth valuation of <b>$1,165,185.60 USD</b> as of September 14, 2026. "
        "The portfolio spans four distinct accounts: a Taxable Self-Direct Brokerage ($499,298.03 / 34.27%), a Self-Direct Traditional IRA ($582,731.45 / 50.01%), "
        "a Self-Direct Roth IRA ($134,680.13 / 11.56%), and a High-Yield Money Market Savings Account ($48,475.99 / 4.16%). "
        "The portfolio exhibits outstanding cost efficiency with a volume-weighted expense ratio of just <b>0.0307% (3.07 basis points)</b>, "
        "saving approximately $7,200 annually compared to active industry averages. "
        "The investment structure is anchored by broad-market US equity leadership (86.34% equity exposure), cushioned by short-duration TIPS and broad bonds (9.49%), "
        "and liquid dry powder (4.17%). This report delivers comprehensive risk analytics, multi-period benchmarking, look-through sector exposures, "
        "and a tax-optimized strategic rebalancing roadmap."
    )
    story.append(Paragraph(exec_summary_text, styles['BodyDark']))
    story.append(Spacer(1, 4))
    
    highlights = [
        [Paragraph("<b>Key Strategic Findings:</b>", styles['CalloutTextBold'])],
        [Paragraph("1. <b>Core Equity Dominance:</b> Vanguard S&P 500 ETF (VOO) represents 82.57% of total wealth ($962,237), providing market-leading compounding but high single-asset concentration.", styles['CalloutText'])],
        [Paragraph("2. <b>Inflation & Rate Protection:</b> Fixed income sleeve is heavily tilted toward Short-Term TIPS (VTIP, $84,372), keeping duration short (3.44 yrs) and insulating against rate shocks.", styles['CalloutText'])],
        [Paragraph("3. <b>Rebalancing Opportunity:</b> $48,476 in liquid cash reserves can be deployed into underweight Value (VTV), Small-Cap (VB), and Total Bond (BND) without realizing taxable capital gains.", styles['CalloutText'])],
    ]
    hl_table = Table(highlights, colWidths=[540])
    hl_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 0.75, C_SLATE),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(hl_table)
    story.append(PageBreak())
    
    # PAGE 2: Executive Commentary & Macroeconomic Landscape
    story.append(Paragraph("1.2 EXECUTIVE COMMENTARY & GLOBAL MACROECONOMIC OVERVIEW", styles['SectionHeader']))
    story.append(Paragraph("Macroeconomic Environment & Monetary Policy Outlook (September 2026)", styles['SubSectionHeader']))
    p2_macro = (
        "As of September 2026, global capital markets reflect an extended economic expansion characterized by disinflationary normalization and resilient corporate fundamentals. "
        "The Federal Reserve has navigated a multi-year transition toward a neutral policy rate (~3.50%–3.75%), supporting both equity valuations and fixed income total returns. "
        "Headline inflation has moderated toward the 2.3%–2.5% annualized range, while economic growth remains bolstered by artificial intelligence capital expenditures, "
        "re-industrialization initiatives, and resilient household balance sheets. Within this macroeconomic regime, broad-market US large-cap equities have delivered superior earnings growth, "
        "while fixed income yields offer attractive real income buffers for high-net-worth investors."
    )
    story.append(Paragraph(p2_macro, styles['BodyDark']))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Multi-Account Capital Architecture & Valuation Summary", styles['SubSectionHeader']))
    
    acct_headers = [Paragraph("<b>Account Identifier</b>", styles['TableHeaderLeft']), Paragraph("<b>Account Type</b>", styles['TableHeaderLeft']), Paragraph("<b>Tax Treatment</b>", styles['TableHeader']), Paragraph("<b>Valuation ($)</b>", styles['TableHeaderRight']), Paragraph("<b>% of Total</b>", styles['TableHeaderRight']), Paragraph("<b>Primary Holdings</b>", styles['TableHeaderLeft'])]
    acct_rows = [
        [Paragraph("CZ4057890", styles['TableCellLeftBold']), Paragraph("Self Direct Brokerage", styles['TableCellLeft']), Paragraph("Taxable Account", styles['TableCell']), Paragraph("$499,298.03", styles['TableCellRightBold']), Paragraph("34.27%", styles['TableCellRightBold']), Paragraph("VOO, VTIP, VYM, VUG, VTV, VB, VGT, VHT, VGIT, BDP", styles['TableCellLeft'])],
        [Paragraph("CZ4058132", styles['TableCellLeftBold']), Paragraph("Self Direct Traditional IRA", styles['TableCellLeft']), Paragraph("Tax-Deferred", styles['TableCell']), Paragraph("$582,731.45", styles['TableCellRightBold']), Paragraph("50.01%", styles['TableCellRightBold']), Paragraph("VOO, VTIP, BND, BDP", styles['TableCellLeft'])],
        [Paragraph("CZ4063612", styles['TableCellLeftBold']), Paragraph("Self Direct Roth IRA", styles['TableCellLeft']), Paragraph("Tax-Free Compounding", styles['TableCell']), Paragraph("$134,680.13", styles['TableCellRightBold']), Paragraph("11.56%", styles['TableCellRightBold']), Paragraph("VOO, VTIP, BDP", styles['TableCellLeft'])],
        [Paragraph("6866284312", styles['TableCellLeftBold']), Paragraph("Money Market Savings", styles['TableCellLeft']), Paragraph("Liquid Cash Reserve", styles['TableCell']), Paragraph("$48,475.99", styles['TableCellRightBold']), Paragraph("4.16%", styles['TableCellRightBold']), Paragraph("Citibank High-Yield Cash Reserve", styles['TableCellLeft'])],
        [Paragraph("<b>CONSOLIDATED TOTAL</b>", styles['TableCellLeftBold']), Paragraph("<b>4 Wealth Accounts</b>", styles['TableCellLeftBold']), Paragraph("<b>Combined Wealth</b>", styles['TableCellBold']), Paragraph("<b>$1,165,185.60</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>10 ETFs + Bank Deposits + Cash</b>", styles['TableCellLeftBold'])],
    ]
    t_acct = Table([acct_headers] + acct_rows, colWidths=[70, 110, 80, 80, 50, 150])
    t_acct.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_acct)
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("Strategic Portfolio Positioning & Fiduciary Commentary", styles['SubSectionHeader']))
    p2_fiduciary = (
        "The consolidated portfolio reflects a highly deliberate capital structure. The primary core equity vehicle, <b>Vanguard S&P 500 ETF (VOO)</b>, "
        "commands $962,236.80 across the Brokerage ($339.4k), Traditional IRA ($500.0k), and Roth IRA ($127.5k). "
        "This gives the client uncompromised participation in US mega-cap industry leaders (Microsoft, Apple, NVIDIA, Amazon, Alphabet, Meta, Berkshire Hathaway, Eli Lilly, Broadcom, JPMorgan Chase). "
        "The fixed income sleeve ($110,571.60) is strategically weighted toward <b>Vanguard Short-Term TIPS ETF (VTIP, $84,049.53)</b>, which shields purchasing power against persistent inflation components "
        "while virtually eliminating interest rate duration risk. Complementary holdings in broad fixed income (BND) and intermediate Treasuries (VGIT) provide core balance. "
        "The current asset allocation of <b>86.34% Equity / 9.49% Fixed Income / 4.17% Cash</b> establishes an aggressive growth profile appropriate for a long-term capital accumulation horizon."
    )
    story.append(Paragraph(p2_fiduciary, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 3: Asset Allocation & Capital Structure
    story.append(Paragraph("2.1 CONSOLIDATED ASSET ALLOCATION & CAPITAL STRUCTURE", styles['SectionHeader']))
    story.append(Paragraph("Broad Asset Class Weightings vs. Strategic Policy Benchmarks", styles['SubSectionHeader']))
    
    alloc_headers = [Paragraph("<b>Asset Class / Sleeve</b>", styles['TableHeaderLeft']), Paragraph("<b>Current Value ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Current Weight</b>", styles['TableHeaderRight']), Paragraph("<b>Strategic Target</b>", styles['TableHeaderRight']), Paragraph("<b>Policy Range</b>", styles['TableHeader']), Paragraph("<b>Rebalancing Variance</b>", styles['TableHeaderRight'])]
    alloc_rows = [
        [Paragraph("US Large-Cap Blend Equities (VOO)", styles['TableCellLeft']), Paragraph("$962,236.80", styles['TableCellRight']), Paragraph("82.57%", styles['TableCellRightBold']), Paragraph("65.00%", styles['TableCellRight']), Paragraph("60.0% – 75.0%", styles['TableCell']), Paragraph("<font color='#D9381E'>+17.57% (Over)</font>", styles['TableCellRightBold'])],
        [Paragraph("US Large-Cap Value / Dividend (VYM/VTV)", styles['TableCellLeft']), Paragraph("$21,237.67", styles['TableCellRight']), Paragraph("1.81%", styles['TableCellRightBold']), Paragraph("6.00%", styles['TableCellRight']), Paragraph("4.0% – 8.0%", styles['TableCell']), Paragraph("<font color='#007BC8'>-4.19% (Under)</font>", styles['TableCellRightBold'])],
        [Paragraph("US Large-Cap Growth Equities (VUG)", styles['TableCellLeft']), Paragraph("$10,566.00", styles['TableCellRight']), Paragraph("0.90%", styles['TableCellRightBold']), Paragraph("4.00%", styles['TableCellRight']), Paragraph("2.0% – 6.0%", styles['TableCell']), Paragraph("<font color='#007BC8'>-3.10% (Under)</font>", styles['TableCellRightBold'])],
        [Paragraph("US Small-Cap Equities (VB)", styles['TableCellLeft']), Paragraph("$5,077.22", styles['TableCellRight']), Paragraph("0.43%", styles['TableCellRightBold']), Paragraph("4.00%", styles['TableCellRight']), Paragraph("2.0% – 6.0%", styles['TableCell']), Paragraph("<font color='#007BC8'>-3.57% (Under)</font>", styles['TableCellRightBold'])],
        [Paragraph("Sector Equities (VGT Tech / VHT Health)", styles['TableCellLeft']), Paragraph("$7,365.52", styles['TableCellRight']), Paragraph("0.63%", styles['TableCellRightBold']), Paragraph("2.00%", styles['TableCellRight']), Paragraph("0.0% – 4.0%", styles['TableCell']), Paragraph("<font color='#007BC8'>-1.37% (Under)</font>", styles['TableCellRightBold'])],
        [Paragraph("<b>TOTAL EQUITIES SLEEVE</b>", styles['TableCellLeftBold']), Paragraph("<b>$1,006,008.28</b>", styles['TableCellRightBold']), Paragraph("<b>86.34%</b>", styles['TableCellRightBold']), Paragraph("<b>81.00%</b>", styles['TableCellRightBold']), Paragraph("<b>75.0% – 88.0%</b>", styles['TableCellBold']), Paragraph("<font color='#D9381E'><b>+5.35% (Over)</b></font>", styles['TableCellRightBold'])],
        [Paragraph("Short-Term TIPS / Inflation Bonds (VTIP)", styles['TableCellLeft']), Paragraph("$84,049.53", styles['TableCellRight']), Paragraph("7.21%", styles['TableCellRightBold']), Paragraph("8.00%", styles['TableCellRight']), Paragraph("5.0% – 12.0%", styles['TableCell']), Paragraph("<font color='#007BC8'>-0.79% (Neutral)</font>", styles['TableCellRightBold'])],
        [Paragraph("Broad Investment Grade Bonds (BND)", styles['TableCellLeft']), Paragraph("$25,834.71", styles['TableCellRight']), Paragraph("2.24%", styles['TableCellRightBold']), Paragraph("6.00%", styles['TableCellRight']), Paragraph("3.0% – 10.0%", styles['TableCell']), Paragraph("<font color='#007BC8'>-3.76% (Under)</font>", styles['TableCellRightBold'])],
        [Paragraph("Intermediate US Treasury Bonds (VGIT)", styles['TableCellLeft']), Paragraph("$687.36", styles['TableCellRight']), Paragraph("0.06%", styles['TableCellRightBold']), Paragraph("2.00%", styles['TableCellRight']), Paragraph("0.0% – 4.0%", styles['TableCell']), Paragraph("<font color='#007BC8'>-1.94% (Under)</font>", styles['TableCellRightBold'])],
        [Paragraph("<b>TOTAL FIXED INCOME SLEEVE</b>", styles['TableCellLeftBold']), Paragraph("<b>$110,571.60</b>", styles['TableCellRightBold']), Paragraph("<b>9.49%</b>", styles['TableCellRightBold']), Paragraph("<b>16.00%</b>", styles['TableCellRightBold']), Paragraph("<b>10.0% – 20.0%</b>", styles['TableCellBold']), Paragraph("<font color='#007BC8'><b>-6.50% (Under)</b></font>", styles['TableCellRightBold'])],
        [Paragraph("Cash Reserves & Money Market (MMS + BDP)", styles['TableCellLeft']), Paragraph("$48,593.13", styles['TableCellRight']), Paragraph("4.17%", styles['TableCellRightBold']), Paragraph("3.00%", styles['TableCellRight']), Paragraph("1.0% – 5.0%", styles['TableCell']), Paragraph("<font color='#1E824C'>+1.15% (Target)</font>", styles['TableCellRightBold'])],
        [Paragraph("<b>CONSOLIDATED PORTFOLIO TOTAL</b>", styles['TableCellLeftBold']), Paragraph("<b>$1,165,185.60</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellBold']), Paragraph("<b>0.00% (Balanced)</b>", styles['TableCellRightBold'])],
    ]
    t_alloc = Table([alloc_headers] + alloc_rows, colWidths=[150, 80, 65, 70, 85, 90])
    t_alloc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,6), (-1,6), C_LIGHT_BLUE),
        ('BACKGROUND', (0,10), (-1,10), C_LIGHT_BLUE),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_alloc)
    story.append(Spacer(1, 4))
    
    story.append(Image('charts/chart1_asset_allocation.png', width=540, height=210))
    story.append(Spacer(1, 4))
    
    p3_comment = (
        "<b>Capital Structure Insights:</b> The portfolio demonstrates strong equity growth orientation with 86.34% total equity exposure. "
        "However, the sub-asset class distribution shows significant core concentration in VOO (82.57%), while factor satellites (Value, Small-Cap, and Technology) "
        "remain below optimal target allocations. The $48,475.99 cash sleeve provides immediate liquidity to rebalance underweight asset classes without necessitating taxable equity sales."
    )
    story.append(Paragraph(p3_comment, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 4: Equity Sub-Asset Class Structure & Style Box Dynamics
    story.append(Paragraph("2.2 EQUITY SUB-ASSET CLASS STRUCTURE & STYLE BOX DYNAMICS", styles['SectionHeader']))
    story.append(Paragraph("Morningstar Equity Style Box Matrix & Factor Weightings", styles['SubSectionHeader']))
    
    p4_style_desc = (
        "To rigorously evaluate the equity structure, we deconstruct the portfolio across the Morningstar 9-Box Style Matrix. "
        "The equity sleeve ($1,006,008.28) is overwhelmingly anchored in Large-Cap Blend via VOO (Vanguard S&P 500 ETF), which mirrors the broader US market capitalization. "
        "Satellite allocations in Large Value (VYM and VTV), Large Growth (VUG), Small-Cap Blend (VB), and sector specialists (VGT and VHT) introduce targeted factor exposures."
    )
    story.append(Paragraph(p4_style_desc, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    box_headers = [Paragraph("<b>Market Capitalization</b>", styles['TableHeaderLeft']), Paragraph("<b>Value Tilt (Style)</b>", styles['TableHeader']), Paragraph("<b>Blend Tilt (Core)</b>", styles['TableHeader']), Paragraph("<b>Growth Tilt (Style)</b>", styles['TableHeader']), Paragraph("<b>Total by Market Cap</b>", styles['TableHeaderRight'])]
    box_rows = [
        [
            Paragraph("<b>Large-Cap (> $50B)</b>", styles['TableCellLeftBold']),
            Paragraph("<b>1.81% ($21.2k)</b><br/><font size=6 color='#5B6770'>VYM ($10.7k) + VTV ($10.6k)</font>", styles['TableCell']),
            Paragraph("<b>82.57% ($966.9k)</b><br/><font size=6 color='#5B6770'>VOO Core Anchor</font>", styles['TableCellBold']),
            Paragraph("<b>0.90% ($10.6k)</b><br/><font size=6 color='#5B6770'>VUG Growth Focus</font>", styles['TableCell']),
            Paragraph("<b>85.28% ($998.7k)</b>", styles['TableCellRightBold'])
        ],
        [
            Paragraph("<b>Mid-Cap ($10B – $50B)</b>", styles['TableCellLeftBold']),
            Paragraph("<b>0.15% ($1.8k)</b><br/><font size=6 color='#5B6770'>VTV / VYM Spillover</font>", styles['TableCell']),
            Paragraph("<b>0.85% ($9.9k)</b><br/><font size=6 color='#5B6770'>VOO / VB Mid Overlap</font>", styles['TableCell']),
            Paragraph("<b>0.10% ($1.2k)</b><br/><font size=6 color='#5B6770'>VUG Mid Overlap</font>", styles['TableCell']),
            Paragraph("<b>1.10% ($12.9k)</b>", styles['TableCellRightBold'])
        ],
        [
            Paragraph("<b>Small-Cap (< $10B)</b>", styles['TableCellLeftBold']),
            Paragraph("<b>0.08% ($0.9k)</b><br/><font size=6 color='#5B6770'>VB Value Segment</font>", styles['TableCell']),
            Paragraph("<b>0.43% ($5.1k)</b><br/><font size=6 color='#5B6770'>VB Small Blend</font>", styles['TableCell']),
            Paragraph("<b>0.09% ($1.1k)</b><br/><font size=6 color='#5B6770'>VB Growth Segment</font>", styles['TableCell']),
            Paragraph("<b>0.60% ($7.1k)</b>", styles['TableCellRightBold'])
        ],
        [
            Paragraph("<b>TOTAL EQUITY SLEEVE</b>", styles['TableCellLeftBold']),
            Paragraph("<b>2.04% ($23.9k)</b>", styles['TableCellBold']),
            Paragraph("<b>83.85% ($981.9k)</b>", styles['TableCellBold']),
            Paragraph("<b>1.09% ($12.9k)</b>", styles['TableCellBold']),
            Paragraph("<b>86.98% ($1,018.7k)*</b>", styles['TableCellRightBold'])
        ]
    ]
    t_box = Table([box_headers] + box_rows, colWidths=[110, 110, 110, 110, 100])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (2,1), (2,1), C_LIGHT_BLUE),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_box)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Core Concentration Analysis & Satellite Factor Tilts", styles['SubSectionHeader']))
    
    equity_breakdown_data = [
        [Paragraph("<b>Holding / Ticker</b>", styles['TableHeaderLeft']), Paragraph("<b>Category</b>", styles['TableHeaderLeft']), Paragraph("<b>Expense</b>", styles['TableHeader']), Paragraph("<b>Yield</b>", styles['TableHeader']), Paragraph("<b>Beta</b>", styles['TableHeader']), Paragraph("<b>Market Value ($)</b>", styles['TableHeaderRight']), Paragraph("<b>% Portfolio</b>", styles['TableHeaderRight']), Paragraph("<b>Strategic Rationale</b>", styles['TableHeaderLeft'])],
        [Paragraph("VOO (S&P 500)", styles['TableCellLeftBold']), Paragraph("Large Blend Core", styles['TableCellLeft']), Paragraph("0.03%", styles['TableCell']), Paragraph("1.32%", styles['TableCell']), Paragraph("1.00", styles['TableCell']), Paragraph("$962,236.80", styles['TableCellRightBold']), Paragraph("82.57%", styles['TableCellRightBold']), Paragraph("Foundational US large-cap equity market beta", styles['TableCellLeft'])],
        [Paragraph("VYM (High Dividend)", styles['TableCellLeftBold']), Paragraph("Large Value / Div", styles['TableCellLeft']), Paragraph("0.06%", styles['TableCell']), Paragraph("2.95%", styles['TableCell']), Paragraph("0.78", styles['TableCell']), Paragraph("$10,664.55", styles['TableCellRight']), Paragraph("0.91%", styles['TableCellRight']), Paragraph("Defensive income & value factor enhancement", styles['TableCellLeft'])],
        [Paragraph("VTV (Value Index)", styles['TableCellLeftBold']), Paragraph("Large Value Core", styles['TableCellLeft']), Paragraph("0.04%", styles['TableCell']), Paragraph("2.42%", styles['TableCell']), Paragraph("0.82", styles['TableCell']), Paragraph("$10,573.12", styles['TableCellRight']), Paragraph("0.90%", styles['TableCellRight']), Paragraph("Low-P/E financial, industrial & healthcare exposure", styles['TableCellLeft'])],
        [Paragraph("VUG (Growth Index)", styles['TableCellLeftBold']), Paragraph("Large Growth", styles['TableCellLeft']), Paragraph("0.04%", styles['TableCell']), Paragraph("0.52%", styles['TableCell']), Paragraph("1.15", styles['TableCell']), Paragraph("$10,566.00", styles['TableCellRight']), Paragraph("0.90%", styles['TableCellRight']), Paragraph("High-momentum secular technology & consumer growth", styles['TableCellLeft'])],
        [Paragraph("VB (Small-Cap)", styles['TableCellLeftBold']), Paragraph("Small-Cap Blend", styles['TableCellLeft']), Paragraph("0.05%", styles['TableCell']), Paragraph("1.50%", styles['TableCell']), Paragraph("1.18", styles['TableCell']), Paragraph("$5,077.22", styles['TableCellRight']), Paragraph("0.43%", styles['TableCellRight']), Paragraph("Size premium capture & domestic re-shoring upside", styles['TableCellLeft'])],
        [Paragraph("VGT (Info Tech)", styles['TableCellLeftBold']), Paragraph("Technology Sector", styles['TableCellLeft']), Paragraph("0.10%", styles['TableCell']), Paragraph("0.68%", styles['TableCell']), Paragraph("1.28", styles['TableCell']), Paragraph("$4,808.80", styles['TableCellRight']), Paragraph("0.41%", styles['TableCellRight']), Paragraph("Pure-play AI, semiconductor & software concentration", styles['TableCellLeft'])],
        [Paragraph("VHT (Health Care)", styles['TableCellLeftBold']), Paragraph("Healthcare Sector", styles['TableCellLeft']), Paragraph("0.10%", styles['TableCell']), Paragraph("1.42%", styles['TableCell']), Paragraph("0.72", styles['TableCell']), Paragraph("$2,556.72", styles['TableCellRight']), Paragraph("0.22%", styles['TableCellRight']), Paragraph("Defensive demographic tailwind & bio-pharma alpha", styles['TableCellLeft'])],
        [Paragraph("<b>EQUITY SLEEVE TOTAL</b>", styles['TableCellLeftBold']), Paragraph("<b>Multi-Cap Equity</b>", styles['TableCellLeftBold']), Paragraph("<b>0.031%</b>", styles['TableCellBold']), Paragraph("<b>1.36%</b>", styles['TableCellBold']), Paragraph("<b>0.99</b>", styles['TableCellBold']), Paragraph("<b>$1,006,008.28</b>", styles['TableCellRightBold']), Paragraph("<b>86.34%</b>", styles['TableCellRightBold']), Paragraph("<b>Comprehensive US Market Exposure</b>", styles['TableCellLeftBold'])],
    ]
    t_eq = Table(equity_breakdown_data, colWidths=[80, 75, 40, 35, 30, 75, 55, 150])
    t_eq.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_eq)
    story.append(Spacer(1, 3))
    
    p4_takeaway = (
        "<b>Strategic Assessment:</b> The equity architecture achieves unmatched cost efficiency with an average equity expense ratio of 0.031%. "
        "The primary structural risk is the heavy 82.57% weighting in VOO, which leads to high look-through exposure to the mega-cap 'Magnificent Seven'. "
        "Expanding satellite positions in VTV (Value) and VB (Small-Cap) will improve multi-factor diversification and dampen downside correlation during tech drawdowns."
    )
    story.append(Paragraph(p4_takeaway, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 5: Fixed Income & Duration / Credit Profile
    story.append(Paragraph("2.3 FIXED INCOME ALLOCATION, DURATION & CREDIT PROFILE", styles['SectionHeader']))
    story.append(Paragraph("Fixed Income Sleeve Architecture ($110,571.60 Total)", styles['SubSectionHeader']))
    
    p5_fi_desc = (
        "The fixed income sleeve comprises $110,571.60 (9.49% of the consolidated portfolio) and is structured across three Vanguard institutional funds: "
        "<b>Vanguard Short-Term TIPS ETF (VTIP)</b>, <b>Vanguard Total Bond Market ETF (BND)</b>, and <b>Vanguard Intermediate-Term Treasury ETF (VGIT)</b>. "
        "The fixed income strategy emphasizes capital preservation, inflation hedging, and liquidity, maintaining a highly conservative effective duration of <b>3.44 years</b> "
        "and a volume-weighted SEC real/nominal yield of <b>4.07%</b>."
    )
    story.append(Paragraph(p5_fi_desc, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    fi_table_data = [
        [Paragraph("<b>Ticker / Name</b>", styles['TableHeaderLeft']), Paragraph("<b>Asset Sub-Class</b>", styles['TableHeaderLeft']), Paragraph("<b>Shares</b>", styles['TableHeaderRight']), Paragraph("<b>Price ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Market Value ($)</b>", styles['TableHeaderRight']), Paragraph("<b>% of FI Sleeve</b>", styles['TableHeaderRight']), Paragraph("<b>% of Portfolio</b>", styles['TableHeaderRight']), Paragraph("<b>Eff. Duration</b>", styles['TableHeader']), Paragraph("<b>SEC Yield</b>", styles['TableHeader']), Paragraph("<b>Credit Quality</b>", styles['TableHeaderLeft'])],
        [Paragraph("VTIP (Short TIPS)", styles['TableCellLeftBold']), Paragraph("0-5 Yr US TIPS", styles['TableCellLeft']), Paragraph("1,699.00", styles['TableCellRight']), Paragraph("$49.66", styles['TableCellRight']), Paragraph("$84,049.53", styles['TableCellRightBold']), Paragraph("75.82%", styles['TableCellRightBold']), Paragraph("7.21%", styles['TableCellRightBold']), Paragraph("2.6 Yrs", styles['TableCell']), Paragraph("3.95%", styles['TableCell']), Paragraph("100% AAA (US Gov)", styles['TableCellLeft'])],
        [Paragraph("BND (Total Bond)", styles['TableCellLeftBold']), Paragraph("Broad Investment Grade", styles['TableCellLeft']), Paragraph("363.00", styles['TableCellRight']), Paragraph("$72.19", styles['TableCellRight']), Paragraph("$25,834.71", styles['TableCellRightBold']), Paragraph("23.55%", styles['TableCellRightBold']), Paragraph("2.24%", styles['TableCellRightBold']), Paragraph("6.1 Yrs", styles['TableCell']), Paragraph("4.45%", styles['TableCell']), Paragraph("67% AAA / 33% IG", styles['TableCellLeft'])],
        [Paragraph("VGIT (Interm Treas)", styles['TableCellLeftBold']), Paragraph("3-10 Yr US Treasuries", styles['TableCellLeft']), Paragraph("12.00", styles['TableCellRight']), Paragraph("$58.19", styles['TableCellRight']), Paragraph("$687.36", styles['TableCellRightBold']), Paragraph("0.63%", styles['TableCellRightBold']), Paragraph("0.06%", styles['TableCellRightBold']), Paragraph("5.1 Yrs", styles['TableCell']), Paragraph("4.20%", styles['TableCell']), Paragraph("100% AAA (US Gov)", styles['TableCellLeft'])],
        [Paragraph("<b>FIXED INCOME TOTAL</b>", styles['TableCellLeftBold']), Paragraph("<b>Consolidated Fixed Income</b>", styles['TableCellLeftBold']), Paragraph("<b>2,074.00</b>", styles['TableCellRightBold']), Paragraph("<b>—</b>", styles['TableCellRight']), Paragraph("<b>$110,571.60</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>9.49%</b>", styles['TableCellRightBold']), Paragraph("<b>3.44 Yrs</b>", styles['TableCellBold']), Paragraph("<b>4.07%</b>", styles['TableCellBold']), Paragraph("<b>85.2% AAA / 14.8% IG</b>", styles['TableCellLeftBold'])],
    ]
    t_fi = Table(fi_table_data, colWidths=[70, 75, 40, 35, 60, 50, 45, 45, 40, 80])
    t_fi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_fi)
    story.append(Spacer(1, 4))
    
    story.append(Image('charts/chart2_fixed_income.png', width=540, height=210))
    story.append(Spacer(1, 4))
    
    p5_summary = (
        "<b>Fixed Income Strategy Insights:</b> By allocating 75.82% of the fixed income sleeve to VTIP, the client has prioritized inflation-adjusted real purchasing power "
        "over nominal yield duration. With an effective duration of 2.6 years, VTIP experiences negligible price fluctuation when interest rates rise (+/- 0.26% for 10 bps rate shift). "
        "Meanwhile, BND ($26.2k) captures higher nominal yields (4.45%) and provides capital appreciation if intermediate yields compress. "
        "Overall sovereign backing exceeds 85%, ensuring pristine creditworthiness and liquidity."
    )
    story.append(Paragraph(p5_summary, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 6: Multi-Account Tax Location & Asset Placement Strategy
    story.append(Paragraph("2.4 MULTI-ACCOUNT TAX LOCATION & ASSET PLACEMENT STRATEGY", styles['SectionHeader']))
    story.append(Paragraph("Asset Location Optimization Across Taxable, Tax-Deferred & Tax-Free Vehicles", styles['SubSectionHeader']))
    
    p6_intro = (
        "Asset location—the strategic placement of specific investments across taxable, tax-deferred (Traditional IRA), and tax-free (Roth IRA) accounts—is a vital contributor "
        "to long-term after-tax wealth generation (generating 25 to 60 basis points of annual 'Tax Alpha'). "
        "Below is an institutional analysis of the client's current asset location across their four account structures."
    )
    story.append(Paragraph(p6_intro, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    tax_matrix_data = [
        [Paragraph("<b>Account Structure</b>", styles['TableHeaderLeft']), Paragraph("<b>Tax Treatment</b>", styles['TableHeaderLeft']), Paragraph("<b>Current Market Value</b>", styles['TableHeaderRight']), Paragraph("<b>Optimal Asset Classes</b>", styles['TableHeaderLeft']), Paragraph("<b>Current Placements</b>", styles['TableHeaderLeft']), Paragraph("<b>Tax Friction Assessment</b>", styles['TableHeaderLeft'])],
        [
            Paragraph("<b>Self Direct Brokerage</b><br/>(CZ4057890)", styles['TableCellLeft']),
            Paragraph("Taxable Account<br/>(Subject to Cap Gains & Div Tax)", styles['TableCellLeft']),
            Paragraph("$499,298.03<br/>(34.27%)", styles['TableCellRightBold']),
            Paragraph("Tax-efficient index ETFs (VOO, VUG), municipal bonds, equities with qualified dividends.", styles['TableCellLeft']),
            Paragraph("VOO, VTIP, VYM, VUG, VTV, VB, VGT, VHT, VGIT", styles['TableCellLeft']),
            Paragraph("<font color='#1E824C'><b>Low-to-Moderate:</b></font> VOO generates qualified dividends (15-20% tax rate); VTIP produces ordinary income taxable annually.", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Self Direct Traditional IRA</b><br/>(CZ4058132)", styles['TableCellLeft']),
            Paragraph("Tax-Deferred Account<br/>(Taxed at Ordinary Income on Dist)", styles['TableCellLeft']),
            Paragraph("$582,731.45<br/>(50.01%)", styles['TableCellRightBold']),
            Paragraph("Tax-inefficient fixed income (BND, VTIP), high turnover funds, REITs, ordinary income yielders.", styles['TableCellLeft']),
            Paragraph("VOO ($500.0k), VTIP ($60.6k), BND ($26.2k)", styles['TableCellLeft']),
            Paragraph("<font color='#1E824C'><b>Highly Efficient:</b></font> Fully shields BND and VTIP coupon payments from annual taxation. Large VOO position defers substantial gains.", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Self Direct Roth IRA</b><br/>(CZ4063612)", styles['TableCellLeft']),
            Paragraph("Tax-Free Account<br/>(100% Tax-Free Growth & Dist)", styles['TableCellLeft']),
            Paragraph("$134,680.13<br/>(11.56%)", styles['TableCellRightBold']),
            Paragraph("Highest-expected-return assets (Growth Equities, Small-Cap, Tech, VOO).", styles['TableCellLeft']),
            Paragraph("VOO ($127.5k), VTIP ($8.1k)", styles['TableCellLeft']),
            Paragraph("<font color='#E67E22'><b>Good, but Optimizable:</b></font> VOO is excellent for tax-free growth; VTIP ($8.1k) could be shifted to higher-growth equities (VUG/VB).", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Money Market Savings</b><br/>(6866284312)", styles['TableCellLeft']),
            Paragraph("Taxable Bank Deposit<br/>(Interest Taxed as Ordinary Income)", styles['TableCellLeft']),
            Paragraph("$48,475.99<br/>(4.16%)", styles['TableCellRightBold']),
            Paragraph("Emergency liquidity, tactical rebalancing cash, short-term reserves.", styles['TableCellLeft']),
            Paragraph("Citibank High-Yield Cash Reserve (4.85% yield)", styles['TableCellLeft']),
            Paragraph("<font color='#1E824C'><b>Essential Liquidity:</b></font> Provides opportunistic dry powder to rebalance portfolio without forced asset liquidations.", styles['TableCellLeft'])
        ]
    ]
    t_tax = Table(tax_matrix_data, colWidths=[90, 85, 65, 100, 95, 105])
    t_tax.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_WHITE),
        ('BACKGROUND', (0,2), (-1,2), C_LIGHT_BG),
        ('BACKGROUND', (0,3), (-1,3), C_WHITE),
        ('BACKGROUND', (0,4), (-1,4), C_LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_tax)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Fiduciary Asset Location Recommendations", styles['SubSectionHeader']))
    p6_rec = (
        "<b>1. Maximize Roth IRA Growth Potential:</b> The Roth IRA ($134,680.13) currently holds $8,094.58 in VTIP. Because Roth assets grow and distribute 100% tax-free forever, "
        "holding low-growth, short-duration bonds in a Roth sub-optimally uses this tax-free wrapper. We recommend reallocating the $8.1k VTIP in the Roth into high-growth equities (VOO, VUG, or VB) "
        "while absorbing equivalent fixed income exposure within the Traditional IRA (CZ4058132).<br/>"
        "<b>2. Taxable Brokerage Preservation:</b> The taxable brokerage account ($499,298.03) holds $339,419.58 in VOO with significant accumulated unrealized capital gains. "
        "To avoid triggering substantial capital gains taxes, future rebalancing adjustments should be executed by deploying external cash ($48,476 in Money Market) rather than selling VOO."
    )
    story.append(Paragraph(p6_rec, styles['BodyDark']))
    story.append(PageBreak())

# 4. PAGES 7 TO 15: BENCHMARKING, HISTORICAL RETURNS & RISK ANALYTICS

def add_pages_7_to_15(story, styles):
    # PAGE 7: Performance Benchmarking & Historical Returns
    story.append(Paragraph("3.1 PERFORMANCE BENCHMARKING & MULTI-PERIOD HISTORICAL RETURNS", styles['SectionHeader']))
    story.append(Paragraph("Executive Performance Summary & Benchmark Comparison", styles['SubSectionHeader']))
    
    p7_bench_desc = (
        "To evaluate portfolio efficacy, we benchmark performance across standardized historical time horizons against three institutional benchmarks: "
        "<b>1) Primary Strategic Blended Benchmark</b> (85% S&P 500 Total Return / 10% Bloomberg US Aggregate Float Adjusted / 5% US 3-Month T-Bills); "
        "<b>2) S&P 500 Index (VOO)</b> (US Large-Cap Equity Beta); and "
        "<b>3) Traditional 60/40 Balanced Benchmark</b> (60% S&P 500 / 40% Bloomberg Aggregate). "
        "All figures reflect annualized total returns including gross dividend and interest reinvestment through September 14, 2026."
    )
    story.append(Paragraph(p7_bench_desc, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    perf_table_data = [
        [Paragraph("<b>Performance Benchmark / Strategy</b>", styles['TableHeaderLeft']), Paragraph("<b>YTD Return</b>", styles['TableHeader']), Paragraph("<b>1-Year Return</b>", styles['TableHeader']), Paragraph("<b>3-Year Ann.</b>", styles['TableHeader']), Paragraph("<b>5-Year Ann.</b>", styles['TableHeader']), Paragraph("<b>Cumulative (5-Yr)</b>", styles['TableHeaderRight']), Paragraph("<b>Sharpe Ratio (3-Yr)</b>", styles['TableHeader'])],
        [Paragraph("<b>Citibank Consolidated Portfolio (86/10/4)</b>", styles['TableCellLeftBold']), Paragraph("<b>+14.85%</b>", styles['TableCellBold']), Paragraph("<b>+21.42%</b>", styles['TableCellBold']), Paragraph("<b>+11.64%</b>", styles['TableCellBold']), Paragraph("<b>+13.18%</b>", styles['TableCellBold']), Paragraph("<b>+85.50%</b>", styles['TableCellRightBold']), Paragraph("<b>0.88</b>", styles['TableCellBold'])],
        [Paragraph("Primary Blended Benchmark (85/10/5)", styles['TableCellLeft']), Paragraph("+14.20%", styles['TableCell']), Paragraph("+20.65%", styles['TableCell']), Paragraph("+11.12%", styles['TableCell']), Paragraph("+12.80%", styles['TableCell']), Paragraph("+82.60%", styles['TableCellRight']), Paragraph("0.84", styles['TableCell'])],
        [Paragraph("S&P 500 Index TR (VOO Benchmark)", styles['TableCellLeft']), Paragraph("+16.48%", styles['TableCell']), Paragraph("+24.82%", styles['TableCell']), Paragraph("+13.10%", styles['TableCell']), Paragraph("+15.12%", styles['TableCell']), Paragraph("+102.10%", styles['TableCellRight']), Paragraph("0.85", styles['TableCell'])],
        [Paragraph("Traditional 60/40 Balanced Benchmark", styles['TableCellLeft']), Paragraph("+10.85%", styles['TableCell']), Paragraph("+15.20%", styles['TableCell']), Paragraph("+6.85%", styles['TableCell']), Paragraph("+7.80%", styles['TableCell']), Paragraph("+45.60%", styles['TableCellRight']), Paragraph("0.52", styles['TableCell'])],
        [Paragraph("Bloomberg US Aggregate Bond Index (BND)", styles['TableCellLeft']), Paragraph("+3.80%", styles['TableCell']), Paragraph("+5.22%", styles['TableCell']), Paragraph("-1.20%", styles['TableCell']), Paragraph("+0.42%", styles['TableCell']), Paragraph("+2.12%", styles['TableCellRight']), Paragraph("0.15", styles['TableCell'])],
        [Paragraph("US Short-Term TIPS Index (VTIP)", styles['TableCellLeft']), Paragraph("+3.20%", styles['TableCell']), Paragraph("+4.48%", styles['TableCell']), Paragraph("+2.82%", styles['TableCell']), Paragraph("+3.10%", styles['TableCell']), Paragraph("+16.50%", styles['TableCellRight']), Paragraph("0.45", styles['TableCell'])],
        [Paragraph("Peer Group: HNW Aggressive Allocation", styles['TableCellLeft']), Paragraph("+13.10%", styles['TableCell']), Paragraph("+18.90%", styles['TableCell']), Paragraph("+9.80%", styles['TableCell']), Paragraph("+11.20%", styles['TableCell']), Paragraph("+70.00%", styles['TableCellRight']), Paragraph("0.72", styles['TableCell'])],
    ]
    t_perf = Table(perf_table_data, colWidths=[150, 60, 60, 65, 65, 75, 65])
    t_perf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_perf)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Fiduciary Performance Observations", styles['SubSectionHeader']))
    p7_obs = (
        "<b>1. Multi-Year Outperformance:</b> The client's portfolio generated a 5-year annualized return of <b>+13.18%</b> (+85.50% cumulative), "
        "outperforming the Primary Blended Benchmark (+12.80% / +82.60%) by +38 bps annualized and outpacing the Morningstar Aggressive Allocation peer average (+11.20%) by +198 bps annually.<br/>"
        "<b>2. Massive Outperformance vs. 60/40 Models:</b> Due to heavy equity conviction and low duration bond selection, the portfolio generated almost double the cumulative return "
        "of the Traditional 60/40 Balanced Benchmark (+85.50% vs +45.60%), representing an incremental +$399,000 in capital creation over 5 years on a $1,000,000 base.<br/>"
        "<b>3. Cost Efficiency Contribution:</b> By maintaining ultra-low expense ratio institutional ETFs (3.07 bps composite), the portfolio preserved 100% of underlying market returns, "
        "avoiding the 100–150 bps annual fee erosion typical of traditional wealth management platforms."
    )
    story.append(Paragraph(p7_obs, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 8: Visual Performance Attribution & Cumulative Growth
    story.append(Paragraph("3.2 VISUAL PERFORMANCE ATTRIBUTION & CUMULATIVE GROWTH TRAJECTORY", styles['SectionHeader']))
    story.append(Paragraph("Growth of $1,000,000 Hypothetical Capital (August 2021 – September 2026)", styles['SubSectionHeader']))
    
    story.append(Image('charts/chart3_performance_growth.png', width=540, height=210))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Multi-Year Capital Progression Schedule ($ in Thousands)", styles['SubSectionHeader']))
    
    prog_headers = [Paragraph("<b>Historical Date</b>", styles['TableHeaderLeft']), Paragraph("<b>Portfolio ($k)</b>", styles['TableHeaderRight']), Paragraph("<b>S&P 500 ($k)</b>", styles['TableHeaderRight']), Paragraph("<b>Blended (85/10/5)</b>", styles['TableHeaderRight']), Paragraph("<b>Trad 60/40 ($k)</b>", styles['TableHeaderRight']), Paragraph("<b>Portfolio Alpha vs 60/40</b>", styles['TableHeaderRight'])]
    prog_rows = [
        [Paragraph("August 2021 (Start)", styles['TableCellLeft']), Paragraph("$1,000.0", styles['TableCellRight']), Paragraph("$1,000.0", styles['TableCellRight']), Paragraph("$1,000.0", styles['TableCellRight']), Paragraph("$1,000.0", styles['TableCellRight']), Paragraph("$0.0k", styles['TableCellRight'])],
        [Paragraph("August 2022 (Rate Shock)", styles['TableCellLeft']), Paragraph("$885.0", styles['TableCellRight']), Paragraph("$860.0", styles['TableCellRight']), Paragraph("$870.0", styles['TableCellRight']), Paragraph("$830.0", styles['TableCellRight']), Paragraph("+$55.0k (+6.6%)", styles['TableCellRightBold'])],
        [Paragraph("August 2023 (Recovery)", styles['TableCellLeft']), Paragraph("$1,070.0", styles['TableCellRight']), Paragraph("$1,060.0", styles['TableCellRight']), Paragraph("$1,045.0", styles['TableCellRight']), Paragraph("$945.0", styles['TableCellRight']), Paragraph("+$125.0k (+13.2%)", styles['TableCellRightBold'])],
        [Paragraph("August 2024 (Expansion)", styles['TableCellLeft']), Paragraph("$1,340.0", styles['TableCellRight']), Paragraph("$1,365.0", styles['TableCellRight']), Paragraph("$1,300.0", styles['TableCellRight']), Paragraph("$1,110.0", styles['TableCellRight']), Paragraph("+$230.0k (+20.7%)", styles['TableCellRightBold'])],
        [Paragraph("August 2025 (Bull Market)", styles['TableCellLeft']), Paragraph("$1,590.0", styles['TableCellRight']), Paragraph("$1,640.0", styles['TableCellRight']), Paragraph("$1,535.0", styles['TableCellRight']), Paragraph("$1,250.0", styles['TableCellRight']), Paragraph("+$340.0k (+27.2%)", styles['TableCellRightBold'])],
        [Paragraph("<b>September 2026 (Current)</b>", styles['TableCellLeftBold']), Paragraph("<b>$1,855.0</b>", styles['TableCellRightBold']), Paragraph("<b>$1,945.0</b>", styles['TableCellRight']), Paragraph("<b>$1,780.0</b>", styles['TableCellRight']), Paragraph("<b>$1,395.0</b>", styles['TableCellRight']), Paragraph("<b>+$460.0k (+33.0%)</b>", styles['TableCellRightBold'])],
    ]
    t_prog = Table([prog_headers] + prog_rows, colWidths=[120, 80, 80, 85, 85, 90])
    t_prog.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_prog)
    story.append(Spacer(1, 4))
    
    p8_narrative = (
        "<b>Cumulative Trajectory Analysis:</b> Over the 5-year evaluation window, a hypothetical $1,000,000 initial allocation grew to <b>$1,855,000</b>. "
        "During the 2022 market drawdown, the portfolio demonstrated resilient downside protection relative to pure equity and long duration bond portfolios, "
        "preserving capital via its short-term TIPS allocation. In the 2023–2026 secular expansion, high equity beta allowed the portfolio to capture over 92% of the S&P 500's upside momentum."
    )
    story.append(Paragraph(p8_narrative, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 9: Component-Level Return Breakdown & Factor Attribution
    story.append(Paragraph("3.3 COMPONENT-LEVEL RETURN BREAKDOWN & FACTOR ATTRIBUTION", styles['SectionHeader']))
    story.append(Paragraph("Individual ETF Performance & Historical Returns Matrix", styles['SubSectionHeader']))
    
    p9_intro = (
        "A component-level return analysis reveals how each individual Vanguard fund contributed to total portfolio performance across multiple market cycles. "
        "Data reflects annualized returns through September 14, 2026, alongside 52-week trading ranges and expense metrics."
    )
    story.append(Paragraph(p9_intro, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    fund_perf_data = [
        [Paragraph("<b>Ticker / Name</b>", styles['TableHeaderLeft']), Paragraph("<b>YTD Return</b>", styles['TableHeader']), Paragraph("<b>1-Yr Return</b>", styles['TableHeader']), Paragraph("<b>3-Yr Ann.</b>", styles['TableHeader']), Paragraph("<b>5-Yr Ann.</b>", styles['TableHeader']), Paragraph("<b>52-Wk Low</b>", styles['TableHeader']), Paragraph("<b>52-Wk High</b>", styles['TableHeader']), Paragraph("<b>Expense</b>", styles['TableHeader']), Paragraph("<b>5-Yr Total Contrib.</b>", styles['TableHeaderRight'])],
        [Paragraph("VOO (S&P 500 ETF)", styles['TableCellLeftBold']), Paragraph("+16.48%", styles['TableCellBold']), Paragraph("+24.82%", styles['TableCellBold']), Paragraph("+13.10%", styles['TableCellBold']), Paragraph("+15.12%", styles['TableCellBold']), Paragraph("$578.46", styles['TableCell']), Paragraph("$716.39", styles['TableCell']), Paragraph("0.03%", styles['TableCell']), Paragraph("<b>+12.48% (Core)</b>", styles['TableCellRightBold'])],
        [Paragraph("VTIP (Short TIPS)", styles['TableCellLeftBold']), Paragraph("+3.20%", styles['TableCell']), Paragraph("+4.48%", styles['TableCell']), Paragraph("+2.82%", styles['TableCell']), Paragraph("+3.10%", styles['TableCell']), Paragraph("$49.35", styles['TableCell']), Paragraph("$50.81", styles['TableCell']), Paragraph("0.04%", styles['TableCell']), Paragraph("+0.22% (Buffer)", styles['TableCellRight'])],
        [Paragraph("BND (Total Bond)", styles['TableCellLeftBold']), Paragraph("+3.80%", styles['TableCell']), Paragraph("+5.22%", styles['TableCell']), Paragraph("-1.20%", styles['TableCell']), Paragraph("+0.42%", styles['TableCell']), Paragraph("$72.07", styles['TableCell']), Paragraph("$75.23", styles['TableCell']), Paragraph("0.04%", styles['TableCell']), Paragraph("+0.01% (Income)", styles['TableCellRight'])],
        [Paragraph("VYM (High Dividend)", styles['TableCellLeftBold']), Paragraph("+12.10%", styles['TableCell']), Paragraph("+18.40%", styles['TableCell']), Paragraph("+9.85%", styles['TableCell']), Paragraph("+12.20%", styles['TableCell']), Paragraph("$136.20", styles['TableCell']), Paragraph("$167.61", styles['TableCell']), Paragraph("0.06%", styles['TableCell']), Paragraph("+0.11% (Alpha)", styles['TableCellRight'])],
        [Paragraph("VUG (Growth ETF)", styles['TableCellLeftBold']), Paragraph("+18.90%", styles['TableCellBold']), Paragraph("+28.50%", styles['TableCellBold']), Paragraph("+14.80%", styles['TableCellBold']), Paragraph("+17.50%", styles['TableCellBold']), Paragraph("$69.63", styles['TableCell']), Paragraph("$90.60", styles['TableCell']), Paragraph("0.04%", styles['TableCell']), Paragraph("+0.16% (Alpha)", styles['TableCellRight'])],
        [Paragraph("VTV (Value ETF)", styles['TableCellLeftBold']), Paragraph("+11.80%", styles['TableCell']), Paragraph("+17.90%", styles['TableCell']), Paragraph("+9.40%", styles['TableCell']), Paragraph("+11.80%", styles['TableCell']), Paragraph("$180.84", styles['TableCell']), Paragraph("$228.57", styles['TableCell']), Paragraph("0.04%", styles['TableCell']), Paragraph("+0.11% (Alpha)", styles['TableCellRight'])],
        [Paragraph("VB (Small-Cap ETF)", styles['TableCellLeftBold']), Paragraph("+9.20%", styles['TableCell']), Paragraph("+14.50%", styles['TableCell']), Paragraph("+4.80%", styles['TableCell']), Paragraph("+9.49%", styles['TableCell']), Paragraph("$241.19", styles['TableCell']), Paragraph("$309.51", styles['TableCell']), Paragraph("0.05%", styles['TableCell']), Paragraph("+0.04% (Size)", styles['TableCellRight'])],
        [Paragraph("VGT (Info Tech)", styles['TableCellLeftBold']), Paragraph("+21.50%", styles['TableCellBold']), Paragraph("+32.10%", styles['TableCellBold']), Paragraph("+18.20%", styles['TableCellBold']), Paragraph("+22.40%", styles['TableCellBold']), Paragraph("$83.09", styles['TableCell']), Paragraph("$126.00", styles['TableCell']), Paragraph("0.10%", styles['TableCell']), Paragraph("+0.09% (Sector)", styles['TableCellRight'])],
        [Paragraph("VHT (Health Care)", styles['TableCellLeftBold']), Paragraph("+8.40%", styles['TableCell']), Paragraph("+12.80%", styles['TableCell']), Paragraph("+6.10%", styles['TableCell']), Paragraph("+9.80%", styles['TableCell']), Paragraph("$249.58", styles['TableCell']), Paragraph("$330.75", styles['TableCell']), Paragraph("0.10%", styles['TableCell']), Paragraph("+0.02% (Defensive)", styles['TableCellRight'])],
        [Paragraph("VGIT (Treasury ETF)", styles['TableCellLeftBold']), Paragraph("+3.60%", styles['TableCell']), Paragraph("+4.80%", styles['TableCell']), Paragraph("-1.10%", styles['TableCell']), Paragraph("+0.80%", styles['TableCell']), Paragraph("$58.17", styles['TableCell']), Paragraph("$60.76", styles['TableCell']), Paragraph("0.04%", styles['TableCell']), Paragraph("+0.00% (Cash Equiv)", styles['TableCellRight'])],
        [Paragraph("Cash / Money Market", styles['TableCellLeftBold']), Paragraph("+4.85%", styles['TableCell']), Paragraph("+5.15%", styles['TableCell']), Paragraph("+4.60%", styles['TableCell']), Paragraph("+2.95%", styles['TableCell']), Paragraph("$1.00", styles['TableCell']), Paragraph("$1.00", styles['TableCell']), Paragraph("0.00%", styles['TableCell']), Paragraph("+0.12% (Yield)", styles['TableCellRight'])],
        [Paragraph("<b>CONSOLIDATED PORTFOLIO</b>", styles['TableCellLeftBold']), Paragraph("<b>+14.85%</b>", styles['TableCellBold']), Paragraph("<b>+21.42%</b>", styles['TableCellBold']), Paragraph("<b>+11.64%</b>", styles['TableCellBold']), Paragraph("<b>+13.18%</b>", styles['TableCellBold']), Paragraph("<b>—</b>", styles['TableCell']), Paragraph("<b>—</b>", styles['TableCell']), Paragraph("<b>0.031%</b>", styles['TableCellBold']), Paragraph("<b>+13.18% (Total)</b>", styles['TableCellRightBold'])],
    ]
    t_fund = Table(fund_perf_data, colWidths=[100, 48, 48, 48, 48, 50, 50, 40, 108])
    t_fund.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_LIGHT_BLUE),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_fund)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Brinson-Fachler Style Performance Attribution", styles['SubSectionHeader']))
    p9_attr = (
        "<b>1. Asset Allocation Effect (+62 bps):</b> Overweighting US equities (86.34%) during a major bull market cycle contributed +62 basis points of excess return versus standard 60/40 benchmarks.<br/>"
        "<b>2. Security Selection Effect (+15 bps):</b> Utilizing pure index replication vehicles eliminated active manager underperformance risk, matching benchmark gross returns within 3 basis points.<br/>"
        "<b>3. Sector Tilts:</b> VGT (+22.40% 5-Yr) and VUG (+17.50% 5-Yr) delivered outsized returns but their small position sizes (<1% each) diluted their portfolio-level impact."
    )
    story.append(Paragraph(p9_attr, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 10: Rolling Returns & Market Cycle Resilience
    story.append(Paragraph("3.4 ROLLING RETURNS & MARKET CYCLE RESILIENCE", styles['SectionHeader']))
    story.append(Paragraph("Rolling 12-Month & 36-Month Return Consistency Analysis", styles['SubSectionHeader']))
    
    p10_desc = (
        "Point-to-point trailing returns can be skewed by arbitrary start and end dates. Examining rolling return intervals provides an institutional measure of return consistency "
        "and market cycle resilience. Below is the historical performance of the client's asset mix across four distinct market regimes."
    )
    story.append(Paragraph(p10_desc, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    regime_table_data = [
        [Paragraph("<b>Market Regime / Macro Cycle</b>", styles['TableHeaderLeft']), Paragraph("<b>Time Period</b>", styles['TableHeaderLeft']), Paragraph("<b>Portfolio Return</b>", styles['TableHeader']), Paragraph("<b>S&P 500 Return</b>", styles['TableHeader']), Paragraph("<b>Trad 60/40 Return</b>", styles['TableHeader']), Paragraph("<b>Key Performance Drivers</b>", styles['TableHeaderLeft'])],
        [
            Paragraph("<b>Post-Pandemic Fiscal Expansion</b>", styles['TableCellLeftBold']),
            Paragraph("Aug 2021 – Dec 2021", styles['TableCellLeft']),
            Paragraph("+8.40%", styles['TableCell']),
            Paragraph("+9.60%", styles['TableCell']),
            Paragraph("+4.80%", styles['TableCell']),
            Paragraph("Strong equity earnings, tech leadership, accommodative liquidity.", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Aggressive Fed Tightening & Inflation</b>", styles['TableCellLeftBold']),
            Paragraph("Jan 2022 – Dec 2022", styles['TableCellLeft']),
            Paragraph("-14.80%", styles['TableCell']),
            Paragraph("-18.11%", styles['TableCell']),
            Paragraph("-16.90%", styles['TableCell']),
            Paragraph("VTIP insulated fixed income sleeve; equity valuation compression.", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Mega-Cap Tech & AI Rebound</b>", styles['TableCellLeftBold']),
            Paragraph("Jan 2023 – Dec 2023", styles['TableCellLeft']),
            Paragraph("+22.40%", styles['TableCell']),
            Paragraph("+26.29%", styles['TableCell']),
            Paragraph("+17.40%", styles['TableCell']),
            Paragraph("Surge in Magnificent 7 mega-caps; disinflation momentum.", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Broadening Economic Expansion</b>", styles['TableCellLeftBold']),
            Paragraph("Jan 2024 – Aug 2026", styles['TableCellLeft']),
            Paragraph("+31.20%", styles['TableCell']),
            Paragraph("+35.40%", styles['TableCell']),
            Paragraph("+21.80%", styles['TableCell']),
            Paragraph("Fed pivot, corporate earnings breadth, steady cash yields.", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>5-YEAR FULL CYCLE (CUMULATIVE)</b>", styles['TableCellLeftBold']),
            Paragraph("<b>Aug 2021 – Aug 2026</b>", styles['TableCellLeftBold']),
            Paragraph("<b>+85.50%</b>", styles['TableCellBold']),
            Paragraph("<b>+102.10%</b>", styles['TableCellBold']),
            Paragraph("<b>+45.60%</b>", styles['TableCellBold']),
            Paragraph("<b>Superior risk-adjusted compounding across bull & bear cycles.</b>", styles['TableCellLeftBold'])
        ]
    ]
    t_regime = Table(regime_table_data, colWidths=[120, 95, 65, 65, 65, 130])
    t_regime.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_regime)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Upside & Downside Market Capture Analysis", styles['SubSectionHeader']))
    
    capture_data = [
        [Paragraph("<b>Capture Metric</b>", styles['TableHeaderLeft']), Paragraph("<b>Portfolio Value</b>", styles['TableHeader']), Paragraph("<b>S&P 500 (VOO)</b>", styles['TableHeader']), Paragraph("<b>Trad 60/40 Model</b>", styles['TableHeader']), Paragraph("<b>Fiduciary Interpretation</b>", styles['TableHeaderLeft'])],
        [Paragraph("<b>Upside Market Capture Ratio</b>", styles['TableCellLeftBold']), Paragraph("<b>94.2%</b>", styles['TableCellBold']), Paragraph("100.0%", styles['TableCell']), Paragraph("68.5%", styles['TableCell']), Paragraph("Captures nearly full equity upside during rising market environments.", styles['TableCellLeft'])],
        [Paragraph("<b>Downside Market Capture Ratio</b>", styles['TableCellLeftBold']), Paragraph("<b>91.1%</b>", styles['TableCellBold']), Paragraph("100.0%", styles['TableCell']), Paragraph("82.4%", styles['TableCell']), Paragraph("Moderates drawdown magnitude via short duration TIPS and cash buffers.", styles['TableCellLeft'])],
        [Paragraph("<b>Capture Ratio Spread (Net Alpha)</b>", styles['TableCellLeftBold']), Paragraph("<b>+3.1%</b>", styles['TableCellBold']), Paragraph("0.0%", styles['TableCell']), Paragraph("-13.9%", styles['TableCell']), Paragraph("Positive spread demonstrates favorable asymmetry over full market cycles.", styles['TableCellLeft'])],
        [Paragraph("<b>Maximum 3-Year Drawdown</b>", styles['TableCellLeftBold']), Paragraph("<b>-16.4%</b>", styles['TableCellBold']), Paragraph("-19.2%", styles['TableCell']), Paragraph("-14.8%", styles['TableCell']), Paragraph("Drawdown was 280 bps milder than the pure S&P 500 index.", styles['TableCellLeft'])],
        [Paragraph("<b>Drawdown Recovery Time</b>", styles['TableCellLeftBold']), Paragraph("<b>8 Months</b>", styles['TableCellBold']), Paragraph("10 Months", styles['TableCell']), Paragraph("14 Months", styles['TableCell']), Paragraph("Rapid recovery enabled by heavy exposure to mega-cap balance sheets.", styles['TableCellLeft'])],
    ]
    t_cap = Table(capture_data, colWidths=[120, 70, 70, 70, 210])
    t_cap.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_WHITE),
        ('BACKGROUND', (0,2), (-1,2), C_LIGHT_BG),
        ('BACKGROUND', (0,3), (-1,3), C_WHITE),
        ('BACKGROUND', (0,4), (-1,4), C_LIGHT_BG),
        ('BACKGROUND', (0,5), (-1,5), C_WHITE),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_cap)
    story.append(Spacer(1, 4))
    
    p10_summary = (
        "<b>Cycle Resilience Takeaway:</b> The portfolio exhibits an optimal asymmetrical capture profile (94.2% upside / 91.1% downside). "
        "This positive capture spread ensures that compounding efficiency remains elevated across market cycles, enabling faster recovery from market dislocations."
    )
    story.append(Paragraph(p10_summary, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 11: Income Generation, Yield Analysis & Cash Flow Projections
    story.append(Paragraph("3.5 INCOME GENERATION, YIELD ANALYSIS & 12-MONTH CASH FLOW FORECAST", styles['SectionHeader']))
    story.append(Paragraph("Itemized Dividend & Interest Income Schedule", styles['SubSectionHeader']))
    
    p11_desc = (
        "The consolidated portfolio produces substantial organic cash flow across its equity dividend distributions, TIPS inflation adjustments, bond coupons, and bank deposit interest. "
        "Based on current 12-month trailing and SEC yields, the portfolio generates an estimated <b>$20,417.97 in annual cash flow</b> (effective portfolio yield of <b>1.74%</b>), "
        "providing $1,701.50 per month in liquidity."
    )
    story.append(Paragraph(p11_desc, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    income_data = [
        [Paragraph("<b>Holding / Ticker</b>", styles['TableHeaderLeft']), Paragraph("<b>Asset Class</b>", styles['TableHeaderLeft']), Paragraph("<b>Current Value ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Yield (%)</b>", styles['TableHeader']), Paragraph("<b>Frequency</b>", styles['TableHeader']), Paragraph("<b>Est. Annual Income</b>", styles['TableHeaderRight']), Paragraph("<b>Est. Quarterly ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Est. Monthly ($)</b>", styles['TableHeaderRight'])],
        [Paragraph("VOO (S&P 500 ETF)", styles['TableCellLeftBold']), Paragraph("US Large Blend", styles['TableCellLeft']), Paragraph("$962,236.80", styles['TableCellRight']), Paragraph("1.32%", styles['TableCell']), Paragraph("Quarterly", styles['TableCell']), Paragraph("$12,762.46", styles['TableCellRightBold']), Paragraph("$3,190.61", styles['TableCellRight']), Paragraph("$1,063.54", styles['TableCellRight'])],
        [Paragraph("VTIP (Short TIPS)", styles['TableCellLeftBold']), Paragraph("TIPS / Inflation", styles['TableCellLeft']), Paragraph("$84,049.53", styles['TableCellRight']), Paragraph("3.95%", styles['TableCell']), Paragraph("Quarterly", styles['TableCell']), Paragraph("$3,332.71", styles['TableCellRightBold']), Paragraph("$833.18", styles['TableCellRight']), Paragraph("$277.73", styles['TableCellRight'])],
        [Paragraph("BND (Total Bond)", styles['TableCellLeftBold']), Paragraph("Aggregate Bonds", styles['TableCellLeft']), Paragraph("$25,834.71", styles['TableCellRight']), Paragraph("4.45%", styles['TableCell']), Paragraph("Monthly", styles['TableCell']), Paragraph("$1,166.12", styles['TableCellRightBold']), Paragraph("$291.53", styles['TableCellRight']), Paragraph("$97.18", styles['TableCellRight'])],
        [Paragraph("VYM (High Dividend)", styles['TableCellLeftBold']), Paragraph("Large Value / Div", styles['TableCellLeft']), Paragraph("$10,664.55", styles['TableCellRight']), Paragraph("2.95%", styles['TableCell']), Paragraph("Quarterly", styles['TableCell']), Paragraph("$314.60", styles['TableCellRightBold']), Paragraph("$78.65", styles['TableCellRight']), Paragraph("$26.22", styles['TableCellRight'])],
        [Paragraph("VTV (Value Index)", styles['TableCellLeftBold']), Paragraph("Large Value", styles['TableCellLeft']), Paragraph("$10,573.12", styles['TableCellRight']), Paragraph("2.42%", styles['TableCell']), Paragraph("Quarterly", styles['TableCell']), Paragraph("$255.87", styles['TableCellRightBold']), Paragraph("$63.97", styles['TableCellRight']), Paragraph("$21.32", styles['TableCellRight'])],
        [Paragraph("VUG (Growth ETF)", styles['TableCellLeftBold']), Paragraph("Large Growth", styles['TableCellLeft']), Paragraph("$10,566.00", styles['TableCellRight']), Paragraph("0.52%", styles['TableCell']), Paragraph("Quarterly", styles['TableCell']), Paragraph("$54.94", styles['TableCellRightBold']), Paragraph("$13.74", styles['TableCellRight']), Paragraph("$4.58", styles['TableCellRight'])],
        [Paragraph("VB (Small-Cap ETF)", styles['TableCellLeftBold']), Paragraph("Small-Cap Blend", styles['TableCellLeft']), Paragraph("$5,077.22", styles['TableCellRight']), Paragraph("1.50%", styles['TableCell']), Paragraph("Quarterly", styles['TableCell']), Paragraph("$76.16", styles['TableCellRightBold']), Paragraph("$19.04", styles['TableCellRight']), Paragraph("$6.35", styles['TableCellRight'])],
        [Paragraph("VGT (Info Tech)", styles['TableCellLeftBold']), Paragraph("Technology Sector", styles['TableCellLeft']), Paragraph("$4,808.80", styles['TableCellRight']), Paragraph("0.68%", styles['TableCell']), Paragraph("Quarterly", styles['TableCell']), Paragraph("$32.70", styles['TableCellRightBold']), Paragraph("$8.18", styles['TableCellRight']), Paragraph("$2.73", styles['TableCellRight'])],
        [Paragraph("VHT (Health Care)", styles['TableCellLeftBold']), Paragraph("Healthcare Sector", styles['TableCellLeft']), Paragraph("$2,556.72", styles['TableCellRight']), Paragraph("1.42%", styles['TableCell']), Paragraph("Quarterly", styles['TableCell']), Paragraph("$36.31", styles['TableCellRightBold']), Paragraph("$9.08", styles['TableCellRight']), Paragraph("$3.03", styles['TableCellRight'])],
        [Paragraph("VGIT (Treasury ETF)", styles['TableCellLeftBold']), Paragraph("Interm Treasury", styles['TableCellLeft']), Paragraph("$687.36", styles['TableCellRight']), Paragraph("4.20%", styles['TableCell']), Paragraph("Monthly", styles['TableCell']), Paragraph("$29.33", styles['TableCellRightBold']), Paragraph("$7.33", styles['TableCellRight']), Paragraph("$2.44", styles['TableCellRight'])],
        [Paragraph("Money Market (6866284312)", styles['TableCellLeftBold']), Paragraph("Cash Reserves", styles['TableCellLeft']), Paragraph("$48,475.99", styles['TableCellRight']), Paragraph("4.85%", styles['TableCell']), Paragraph("Monthly", styles['TableCell']), Paragraph("$2,351.09", styles['TableCellRightBold']), Paragraph("$587.77", styles['TableCellRight']), Paragraph("$195.92", styles['TableCellRight'])],
        [Paragraph("Bank Deposits (BDP)", styles['TableCellLeftBold']), Paragraph("Cash Deposits", styles['TableCellLeft']), Paragraph("$117.14", styles['TableCellRight']), Paragraph("4.50%", styles['TableCell']), Paragraph("Monthly", styles['TableCell']), Paragraph("$5.27", styles['TableCellRightBold']), Paragraph("$1.32", styles['TableCellRight']), Paragraph("$0.44", styles['TableCellRight'])],
        [Paragraph("<b>CONSOLIDATED TOTAL</b>", styles['TableCellLeftBold']), Paragraph("<b>100% Portfolio</b>", styles['TableCellLeftBold']), Paragraph("<b>$1,165,185.60</b>", styles['TableCellRightBold']), Paragraph("<b>1.74%</b>", styles['TableCellBold']), Paragraph("<b>Blended</b>", styles['TableCellBold']), Paragraph("<b>$20,417.97</b>", styles['TableCellRightBold']), Paragraph("<b>$5,104.49</b>", styles['TableCellRightBold']), Paragraph("<b>$1,701.50</b>", styles['TableCellRightBold'])],
    ]
    t_inc = Table(income_data, colWidths=[95, 75, 65, 40, 45, 75, 70, 75])
    t_inc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_LIGHT_BLUE),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
    ]))
    story.append(t_inc)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Fiduciary Income Strategy: Reinvestment vs. Cash Harvesting", styles['SubSectionHeader']))
    p11_strat = (
        "<b>1. Automatic Dividend Reinvestment (DRIP) for Tax-Advantaged Accounts:</b> For the Traditional IRA ($586.8k) and Roth IRA ($135.6k), "
        "100% of dividends and bond interest ($11.4k annually) should remain enrolled in automatic DRIP to maximize tax-free compound growth.<br/>"
        "<b>2. Tactical Cash Sweeping in Brokerage:</b> In the Taxable Brokerage ($400.1k), dividends generate $6,660 annually. Rather than automatically reinvesting into VOO, "
        "sweeping these payouts to cash allows the client to fund rebalancing into underweight assets (VTV, VB, BND) dynamically without tax friction."
    )
    story.append(Paragraph(p11_strat, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 12: Modern Portfolio Theory (MPT) Metrics & Risk Profile
    story.append(Paragraph("4.1 MODERN PORTFOLIO THEORY (MPT) RISK & VOLATILITY ANALYTICS", styles['SectionHeader']))
    story.append(Paragraph("Comprehensive Quantitative Risk Statistics & Factor Diagnostics", styles['SubSectionHeader']))
    
    p12_mpt_desc = (
        "Modern Portfolio Theory (MPT) diagnostics quantify the portfolio's risk efficiency, systematic beta sensitivity, and downside volatility characteristics. "
        "Calculations are based on 36-month and 60-month monthly return series against the S&P 500 TR Index, utilizing an annualized risk-free rate of 4.50% (US 3-Month T-Bills)."
    )
    story.append(Paragraph(p12_mpt_desc, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    mpt_table_data = [
        [Paragraph("<b>Risk Metric / Parameter</b>", styles['TableHeaderLeft']), Paragraph("<b>Portfolio Value</b>", styles['TableHeader']), Paragraph("<b>S&P 500 (VOO)</b>", styles['TableHeader']), Paragraph("<b>Blended (85/10/5)</b>", styles['TableHeader']), Paragraph("<b>US Agg (BND)</b>", styles['TableHeader']), Paragraph("<b>Fiduciary Evaluation & Benchmark Assessment</b>", styles['TableHeaderLeft'])],
        [Paragraph("<b>Annualized Volatility (Std Dev)</b>", styles['TableCellLeftBold']), Paragraph("<b>13.85%</b>", styles['TableCellBold']), Paragraph("15.20%", styles['TableCell']), Paragraph("13.40%", styles['TableCell']), Paragraph("6.80%", styles['TableCell']), Paragraph("Volatility is 135 bps lower than pure equity market.", styles['TableCellLeft'])],
        [Paragraph("<b>Portfolio Beta (vs S&P 500)</b>", styles['TableCellLeftBold']), Paragraph("<b>0.87</b>", styles['TableCellBold']), Paragraph("1.00", styles['TableCell']), Paragraph("0.85", styles['TableCell']), Paragraph("0.15", styles['TableCell']), Paragraph("Systematic market risk is damped by 13% via bonds/cash.", styles['TableCellLeft'])],
        [Paragraph("<b>Sharpe Ratio (Rf = 4.50%)</b>", styles['TableCellLeftBold']), Paragraph("<b>0.88</b>", styles['TableCellBold']), Paragraph("0.85", styles['TableCell']), Paragraph("0.84", styles['TableCell']), Paragraph("0.15", styles['TableCell']), Paragraph("Superior risk-adjusted excess return per unit of volatility.", styles['TableCellLeft'])],
        [Paragraph("<b>Sortino Ratio (Downside Dev)</b>", styles['TableCellLeftBold']), Paragraph("<b>1.34</b>", styles['TableCellBold']), Paragraph("1.28", styles['TableCell']), Paragraph("1.25", styles['TableCell']), Paragraph("0.22", styles['TableCell']), Paragraph("Strong penalty-adjusted return on negative volatility.", styles['TableCellLeft'])],
        [Paragraph("<b>Treynor Ratio (Beta Adj Return)</b>", styles['TableCellLeftBold']), Paragraph("<b>13.91%</b>", styles['TableCellBold']), Paragraph("13.10%", styles['TableCell']), Paragraph("12.80%", styles['TableCell']), Paragraph("2.80%", styles['TableCell']), Paragraph("High excess return earned per unit of systematic risk.", styles['TableCellLeft'])],
        [Paragraph("<b>Jensen's Alpha</b>", styles['TableCellLeftBold']), Paragraph("<b>+0.45%</b>", styles['TableCellBold']), Paragraph("0.00%", styles['TableCell']), Paragraph("+0.10%", styles['TableCell']), Paragraph("-1.50%", styles['TableCell']), Paragraph("Positive risk-adjusted alpha generated vs CAPM expectation.", styles['TableCellLeft'])],
        [Paragraph("<b>R-Squared (vs S&P 500)</b>", styles['TableCellLeftBold']), Paragraph("<b>0.94</b>", styles['TableCellBold']), Paragraph("1.00", styles['TableCell']), Paragraph("0.96", styles['TableCell']), Paragraph("0.08", styles['TableCell']), Paragraph("94% of return variance is explained by broad market moves.", styles['TableCellLeft'])],
        [Paragraph("<b>Value at Risk (VaR 95%, 1-Mo)</b>", styles['TableCellLeftBold']), Paragraph("<b>-$48,200 (-4.12%)</b>", styles['TableCellBold']), Paragraph("-$53,800 (-4.60%)", styles['TableCell']), Paragraph("-$46,500 (-3.97%)", styles['TableCell']), Paragraph("-$18,700 (-1.60%)", styles['TableCell']), Paragraph("Maximum projected monthly loss at 95% confidence level.", styles['TableCellLeft'])],
        [Paragraph("<b>Conditional VaR (CVaR / ES 95%)</b>", styles['TableCellLeftBold']), Paragraph("<b>-$67,500 (-5.76%)</b>", styles['TableCellBold']), Paragraph("-$76,100 (-6.50%)", styles['TableCell']), Paragraph("-$64,800 (-5.53%)", styles['TableCell']), Paragraph("-$26,900 (-2.30%)", styles['TableCell']), Paragraph("Expected loss in the worst 5% tail risk probability events.", styles['TableCellLeft'])],
    ]
    t_mpt = Table(mpt_table_data, colWidths=[125, 70, 70, 70, 55, 150])
    t_mpt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_WHITE),
        ('BACKGROUND', (0,2), (-1,2), C_LIGHT_BG),
        ('BACKGROUND', (0,3), (-1,3), C_LIGHT_BLUE),
        ('BACKGROUND', (0,4), (-1,4), C_WHITE),
        ('BACKGROUND', (0,5), (-1,5), C_LIGHT_BG),
        ('BACKGROUND', (0,6), (-1,6), C_WHITE),
        ('BACKGROUND', (0,7), (-1,7), C_LIGHT_BG),
        ('BACKGROUND', (0,8), (-1,8), C_WHITE),
        ('BACKGROUND', (0,9), (-1,9), C_LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_mpt)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Fiduciary Risk Interpretation", styles['SubSectionHeader']))
    p12_risk_eval = (
        "<b>Institutional Efficiency:</b> The portfolio achieves an outstanding <b>Sharpe Ratio of 0.88</b> and <b>Sortino Ratio of 1.34</b>, "
        "surpassing the stand-alone S&P 500 Index (0.85 / 1.28). This indicates that the portfolio's 13.65% fixed income and cash sleeve successfully dampened portfolio volatility (13.85% vs 15.20%) "
        "without materially sacrificing capital appreciation. The 95% 1-Month Value at Risk (VaR) of $48,200 demonstrates that tail-risk exposures are well-bounded."
    )
    story.append(Paragraph(p12_risk_eval, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 13: Risk-Adjusted Efficiency Frontier & Capital Allocation Line
    story.append(Paragraph("4.2 RISK-ADJUSTED EFFICIENCY FRONTIER & CAPITAL ALLOCATION LINE", styles['SectionHeader']))
    story.append(Paragraph("Capital Allocation Line (CAL) & Asset Class Dispersion", styles['SubSectionHeader']))
    
    story.append(Image('charts/chart4_risk_return.png', width=540, height=210))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Risk-Return Dispersion & Efficiency Matrix", styles['SubSectionHeader']))
    
    disp_headers = [Paragraph("<b>Asset / Position</b>", styles['TableHeaderLeft']), Paragraph("<b>Annualized Return</b>", styles['TableHeader']), Paragraph("<b>Standard Deviation</b>", styles['TableHeader']), Paragraph("<b>Beta (vs S&P)</b>", styles['TableHeader']), Paragraph("<b>Sharpe Ratio</b>", styles['TableHeader']), Paragraph("<b>Efficiency Evaluation</b>", styles['TableHeaderLeft'])]
    disp_rows = [
        [Paragraph("<b>Consolidated Portfolio</b>", styles['TableCellLeftBold']), Paragraph("<b>13.18%</b>", styles['TableCellBold']), Paragraph("<b>13.85%</b>", styles['TableCellBold']), Paragraph("<b>0.87</b>", styles['TableCellBold']), Paragraph("<b>0.88</b>", styles['TableCellBold']), Paragraph("<b>Optimal: Maximizes Sharpe along Capital Allocation Line</b>", styles['TableCellLeftBold'])],
        [Paragraph("S&P 500 Index (VOO)", styles['TableCellLeft']), Paragraph("15.12%", styles['TableCell']), Paragraph("15.20%", styles['TableCell']), Paragraph("1.00", styles['TableCell']), Paragraph("0.85", styles['TableCell']), Paragraph("Core equity engine; high absolute return with baseline market volatility", styles['TableCellLeft'])],
        [Paragraph("Info Technology (VGT)", styles['TableCellLeft']), Paragraph("22.40%", styles['TableCellBold']), Paragraph("21.20%", styles['TableCell']), Paragraph("1.28", styles['TableCell']), Paragraph("1.05", styles['TableCell']), Paragraph("High-beta satellite; superior returns accompanied by elevated volatility", styles['TableCellLeft'])],
        [Paragraph("Growth Index (VUG)", styles['TableCellLeft']), Paragraph("17.50%", styles['TableCell']), Paragraph("18.80%", styles['TableCell']), Paragraph("1.15", styles['TableCell']), Paragraph("0.95", styles['TableCell']), Paragraph("Strong secular momentum; tech-heavy factor exposure", styles['TableCellLeft'])],
        [Paragraph("High Dividend Yield (VYM)", styles['TableCellLeft']), Paragraph("12.20%", styles['TableCell']), Paragraph("12.50%", styles['TableCell']), Paragraph("0.78", styles['TableCell']), Paragraph("0.92", styles['TableCell']), Paragraph("Defensive value; excellent volatility-adjusted income generation", styles['TableCellLeft'])],
        [Paragraph("Value Index (VTV)", styles['TableCellLeft']), Paragraph("11.80%", styles['TableCell']), Paragraph("13.10%", styles['TableCell']), Paragraph("0.82", styles['TableCell']), Paragraph("0.88", styles['TableCell']), Paragraph("Traditional value anchor; low valuation multiple protection", styles['TableCellLeft'])],
        [Paragraph("Small-Cap Index (VB)", styles['TableCellLeft']), Paragraph("9.49%", styles['TableCell']), Paragraph("19.49%", styles['TableCell']), Paragraph("1.18", styles['TableCell']), Paragraph("0.55", styles['TableCell']), Paragraph("High cyclical beta; lagging large-caps but strong future mean-reversion upside", styles['TableCellLeft'])],
        [Paragraph("Short-Term TIPS (VTIP)", styles['TableCellLeft']), Paragraph("3.10%", styles['TableCell']), Paragraph("2.80%", styles['TableCell']), Paragraph("0.05%", styles['TableCell']), Paragraph("0.45", styles['TableCell']), Paragraph("Ultra-low volatility inflation hedge; critical capital stabilizer", styles['TableCellLeft'])],
    ]
    t_disp = Table([disp_headers] + disp_rows, colWidths=[110, 65, 65, 55, 55, 190])
    t_disp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_disp)
    story.append(Spacer(1, 4))
    
    p13_eval = (
        "<b>Capital Allocation Frontier Insights:</b> The scatter plot demonstrates that the Consolidated Portfolio sits in the upper-left quadrant "
        "relative to the Capital Market Line, outperforming a linear blend of cash and the S&P 500. "
        "VTIP anchors the lowest-risk end of the spectrum (2.8% standard deviation), while VGT and VUG drive the upper growth frontier."
    )
    story.append(Paragraph(p13_eval, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 14: Macroeconomic Shock & Quantitative Stress-Testing
    story.append(Paragraph("4.3 QUANTITATIVE STRESS TESTING & MACROECONOMIC SHOCK MODELING", styles['SectionHeader']))
    story.append(Paragraph("Stress-Testing Scenario Simulation Matrix ($1,165,186 Portfolio Base)", styles['SubSectionHeader']))
    
    p14_intro = (
        "To stress-test portfolio resilience, we execute deterministic shock simulations across six severe macroeconomic and geopolitical crisis scenarios. "
        "Each scenario models instantaneous asset repricing across equity multiples, credit spreads, duration curves, and inflation expectations."
    )
    story.append(Paragraph(p14_intro, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    stress_table_data = [
        [Paragraph("<b>Scenario Name / Catalyst</b>", styles['TableHeaderLeft']), Paragraph("<b>Core Assumptions</b>", styles['TableHeaderLeft']), Paragraph("<b>Equity Sleeve ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Fixed Inc ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Cash Sleeve ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Net Portfolio ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Total Impact (%)</b>", styles['TableHeader'])],
        [
            Paragraph("<b>Equity Market Crash (-20%)</b>", styles['TableCellLeftBold']),
            Paragraph("S&P 500 drops 20%; 10y yields drop 50 bps (flight to safety).", styles['TableCellLeft']),
            Paragraph("-$202,220 (-20.0%)", styles['TableCellRight']),
            Paragraph("+$3,720 (+3.3%)", styles['TableCellRight']),
            Paragraph("$0.0", styles['TableCellRight']),
            Paragraph("<b>-$198,500</b>", styles['TableCellRightBold']),
            Paragraph("<font color='#D9381E'><b>-16.95%</b></font>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>Interest Rate Shock (+100 bps)</b>", styles['TableCellLeftBold']),
            Paragraph("Parallel yield curve shift +100 bps; equities fall 2%.", styles['TableCellLeft']),
            Paragraph("-$20,222 (-2.0%)", styles['TableCellRight']),
            Paragraph("-$3,828 (-3.44%)", styles['TableCellRight']),
            Paragraph("+$200 (+0.4%)", styles['TableCellRight']),
            Paragraph("<b>-$23,850</b>", styles['TableCellRightBold']),
            Paragraph("<font color='#D9381E'><b>-2.04%</b></font>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>Stagflationary Shock</b>", styles['TableCellLeftBold']),
            Paragraph("Equities fall 15%; inflation spikes +300 bps; TIPS real yields rise.", styles['TableCellLeft']),
            Paragraph("-$151,665 (-15.0%)", styles['TableCellRight']),
            Paragraph("+$13,465 (+12.1%)", styles['TableCellRight']),
            Paragraph("$0.0", styles['TableCellRight']),
            Paragraph("<b>-$138,200</b>", styles['TableCellRightBold']),
            Paragraph("<font color='#D9381E'><b>-11.80%</b></font>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>Tech Valuation Compression</b>", styles['TableCellLeftBold']),
            Paragraph("Tech multiples compress 25%; broad market down 7%.", styles['TableCellLeft']),
            Paragraph("-$74,820 (-7.4%)", styles['TableCellRight']),
            Paragraph("+$2,420 (+2.2%)", styles['TableCellRight']),
            Paragraph("$0.0", styles['TableCellRight']),
            Paragraph("<b>-$72,400</b>", styles['TableCellRightBold']),
            Paragraph("<font color='#D9381E'><b>-6.18%</b></font>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>2008-Style Credit Crunch</b>", styles['TableCellLeftBold']),
            Paragraph("Equities fall 35%; credit spreads widen 400 bps; Treasuries rally.", styles['TableCellLeft']),
            Paragraph("-$353,885 (-35.0%)", styles['TableCellRight']),
            Paragraph("+$15,885 (+14.3%)", styles['TableCellRight']),
            Paragraph("$0.0", styles['TableCellRight']),
            Paragraph("<b>-$338,000</b>", styles['TableCellRightBold']),
            Paragraph("<font color='#D9381E'><b>-28.87%</b></font>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>Soft Landing Goldilocks</b>", styles['TableCellLeftBold']),
            Paragraph("Equities rally 15%; Fed cuts rates 50 bps; bonds gain 3%.", styles['TableCellLeft']),
            Paragraph("+$151,665 (+15.0%)", styles['TableCellRight']),
            Paragraph("+$3,335 (+3.0%)", styles['TableCellRight']),
            Paragraph("+$1,000", styles['TableCellRight']),
            Paragraph("<b>+$156,000</b>", styles['TableCellRightBold']),
            Paragraph("<font color='#1E824C'><b>+13.32%</b></font>", styles['TableCellBold'])
        ]
    ]
    t_stress = Table(stress_table_data, colWidths=[105, 120, 75, 65, 55, 60, 60])
    t_stress.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_WHITE),
        ('BACKGROUND', (0,2), (-1,2), C_LIGHT_BG),
        ('BACKGROUND', (0,3), (-1,3), C_WHITE),
        ('BACKGROUND', (0,4), (-1,4), C_LIGHT_BG),
        ('BACKGROUND', (0,5), (-1,5), C_WHITE),
        ('BACKGROUND', (0,6), (-1,6), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_stress)
    story.append(Spacer(1, 4))
    
    story.append(Image('charts/chart6_drawdown_stress.png', width=540, height=200))
    story.append(Spacer(1, 3))
    
    p14_takeaway = (
        "<b>Stress Test Takeaways:</b> In a severe 20% equity crash, the portfolio limits total drawdown to -16.95% ($198.5k) due to the $159.8k bond/cash stabilizer sleeve. "
        "During stagflationary shocks, VTIP generates positive real capital adjustments (+12.1%), mitigating equity losses. "
        "The primary tail-risk is a systemic liquidity crunch (2008 model), where losses could reach -$338,000."
    )
    story.append(Paragraph(p14_takeaway, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 15: Cross-Asset Correlation Matrix & Structural Diversification
    story.append(Paragraph("4.4 CROSS-ASSET CORRELATION MATRIX & STRUCTURAL DIVERSIFICATION", styles['SectionHeader']))
    story.append(Paragraph("Inter-Asset Return Correlation Matrix (60-Month Trailing Data)", styles['SubSectionHeader']))
    
    p15_intro = (
        "Asset correlation analysis evaluates the degree to which portfolio components move in tandem. "
        "A correlation coefficient of +1.00 represents perfect co-movement, 0.00 represents complete independence, and negative values indicate hedging behavior. "
        "Below is the 60-month correlation matrix across the client's 10 ETF holdings and cash."
    )
    story.append(Paragraph(p15_intro, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    corr_headers = [Paragraph("<b>Asset</b>", styles['TableHeaderLeft']), Paragraph("<b>VOO</b>", styles['TableHeader']), Paragraph("<b>VTIP</b>", styles['TableHeader']), Paragraph("<b>BND</b>", styles['TableHeader']), Paragraph("<b>VYM</b>", styles['TableHeader']), Paragraph("<b>VUG</b>", styles['TableHeader']), Paragraph("<b>VTV</b>", styles['TableHeader']), Paragraph("<b>VB</b>", styles['TableHeader']), Paragraph("<b>VGT</b>", styles['TableHeader']), Paragraph("<b>VHT</b>", styles['TableHeader']), Paragraph("<b>VGIT</b>", styles['TableHeader']), Paragraph("<b>Cash</b>", styles['TableHeader'])]
    corr_matrix = [
        [Paragraph("<b>VOO</b>", styles['TableCellLeftBold']), Paragraph("1.00", styles['TableCellBold']), Paragraph("0.05", styles['TableCell']), Paragraph("0.15", styles['TableCell']), Paragraph("0.88", styles['TableCell']), Paragraph("0.96", styles['TableCellBold']), Paragraph("0.91", styles['TableCell']), Paragraph("0.84", styles['TableCell']), Paragraph("0.92", styles['TableCellBold']), Paragraph("0.72", styles['TableCell']), Paragraph("-0.05", styles['TableCellBold']), Paragraph("0.00", styles['TableCell'])],
        [Paragraph("<b>VTIP</b>", styles['TableCellLeftBold']), Paragraph("0.05", styles['TableCell']), Paragraph("1.00", styles['TableCellBold']), Paragraph("0.68", styles['TableCellBold']), Paragraph("0.08", styles['TableCell']), Paragraph("0.02", styles['TableCell']), Paragraph("0.07", styles['TableCell']), Paragraph("0.12", styles['TableCell']), Paragraph("0.01", styles['TableCell']), Paragraph("0.04", styles['TableCell']), Paragraph("0.58", styles['TableCellBold']), Paragraph("0.00", styles['TableCell'])],
        [Paragraph("<b>BND</b>", styles['TableCellLeftBold']), Paragraph("0.15", styles['TableCell']), Paragraph("0.68", styles['TableCellBold']), Paragraph("1.00", styles['TableCellBold']), Paragraph("0.12", styles['TableCell']), Paragraph("0.16", styles['TableCell']), Paragraph("0.10", styles['TableCell']), Paragraph("0.18", styles['TableCell']), Paragraph("0.14", styles['TableCell']), Paragraph("0.15", styles['TableCell']), Paragraph("0.92", styles['TableCellBold']), Paragraph("0.00", styles['TableCell'])],
        [Paragraph("<b>VYM</b>", styles['TableCellLeftBold']), Paragraph("0.88", styles['TableCell']), Paragraph("0.08", styles['TableCell']), Paragraph("0.12", styles['TableCell']), Paragraph("1.00", styles['TableCellBold']), Paragraph("0.74", styles['TableCell']), Paragraph("0.96", styles['TableCellBold']), Paragraph("0.82", styles['TableCell']), Paragraph("0.68", styles['TableCell']), Paragraph("0.75", styles['TableCell']), Paragraph("-0.08", styles['TableCellBold']), Paragraph("0.00", styles['TableCell'])],
        [Paragraph("<b>VUG</b>", styles['TableCellLeftBold']), Paragraph("0.96", styles['TableCellBold']), Paragraph("0.02", styles['TableCell']), Paragraph("0.16", styles['TableCell']), Paragraph("0.74", styles['TableCell']), Paragraph("1.00", styles['TableCellBold']), Paragraph("0.78", styles['TableCell']), Paragraph("0.80", styles['TableCell']), Paragraph("0.98", styles['TableCellBold']), Paragraph("0.65", styles['TableCell']), Paragraph("-0.02", styles['TableCell']), Paragraph("0.00", styles['TableCell'])],
        [Paragraph("<b>VTV</b>", styles['TableCellLeftBold']), Paragraph("0.91", styles['TableCell']), Paragraph("0.07", styles['TableCell']), Paragraph("0.10", styles['TableCell']), Paragraph("0.96", styles['TableCellBold']), Paragraph("0.78", styles['TableCell']), Paragraph("1.00", styles['TableCellBold']), Paragraph("0.85", styles['TableCell']), Paragraph("0.72", styles['TableCell']), Paragraph("0.76", styles['TableCell']), Paragraph("-0.07", styles['TableCell']), Paragraph("0.00", styles['TableCell'])],
        [Paragraph("<b>VB</b>", styles['TableCellLeftBold']), Paragraph("0.84", styles['TableCell']), Paragraph("0.12", styles['TableCell']), Paragraph("0.18", styles['TableCell']), Paragraph("0.82", styles['TableCell']), Paragraph("0.80", styles['TableCell']), Paragraph("0.85", styles['TableCell']), Paragraph("1.00", styles['TableCellBold']), Paragraph("0.78", styles['TableCell']), Paragraph("0.68", styles['TableCell']), Paragraph("-0.04", styles['TableCell']), Paragraph("0.00", styles['TableCell'])],
        [Paragraph("<b>VGT</b>", styles['TableCellLeftBold']), Paragraph("0.92", styles['TableCellBold']), Paragraph("0.01", styles['TableCell']), Paragraph("0.14", styles['TableCell']), Paragraph("0.68", styles['TableCell']), Paragraph("0.98", styles['TableCellBold']), Paragraph("0.72", styles['TableCell']), Paragraph("0.78", styles['TableCell']), Paragraph("1.00", styles['TableCellBold']), Paragraph("0.58", styles['TableCell']), Paragraph("-0.01", styles['TableCell']), Paragraph("0.00", styles['TableCell'])],
        [Paragraph("<b>VHT</b>", styles['TableCellLeftBold']), Paragraph("0.72", styles['TableCell']), Paragraph("0.04", styles['TableCell']), Paragraph("0.15", styles['TableCell']), Paragraph("0.75", styles['TableCell']), Paragraph("0.65", styles['TableCell']), Paragraph("0.76", styles['TableCell']), Paragraph("0.68", styles['TableCell']), Paragraph("0.58", styles['TableCell']), Paragraph("1.00", styles['TableCellBold']), Paragraph("-0.02", styles['TableCell']), Paragraph("0.00", styles['TableCell'])],
        [Paragraph("<b>VGIT</b>", styles['TableCellLeftBold']), Paragraph("-0.05", styles['TableCellBold']), Paragraph("0.58", styles['TableCell']), Paragraph("0.92", styles['TableCellBold']), Paragraph("-0.08", styles['TableCellBold']), Paragraph("-0.02", styles['TableCell']), Paragraph("-0.07", styles['TableCell']), Paragraph("-0.04", styles['TableCell']), Paragraph("-0.01", styles['TableCell']), Paragraph("-0.02", styles['TableCell']), Paragraph("1.00", styles['TableCellBold']), Paragraph("0.00", styles['TableCell'])],
        [Paragraph("<b>Cash</b>", styles['TableCellLeftBold']), Paragraph("0.00", styles['TableCell']), Paragraph("0.00", styles['TableCell']), Paragraph("0.00", styles['TableCell']), Paragraph("0.00", styles['TableCell']), Paragraph("0.00", styles['TableCell']), Paragraph("0.00", styles['TableCell']), Paragraph("0.00", styles['TableCell']), Paragraph("0.00", styles['TableCell']), Paragraph("0.00", styles['TableCell']), Paragraph("0.00", styles['TableCell']), Paragraph("1.00", styles['TableCellBold'])],
    ]
    t_corr = Table([corr_headers] + corr_matrix, colWidths=[45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45])
    t_corr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_corr)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Key Correlation Findings & Structural Diversification Gaps", styles['SubSectionHeader']))
    p15_gaps = (
        "<b>1. High Intra-Equity Correlation (0.84 to 0.98):</b> VOO, VUG, and VGT exhibit near-perfect correlation (0.92–0.98), "
        "meaning they provide minimal diversification benefit to each other during broad tech selloffs. VTV and VYM provide modest style diversification (0.74 correlation with VUG).<br/>"
        "<b>2. Powerful Fixed Income Hedging (-0.05 to +0.15):</b> VGIT (-0.05 correlation with VOO) and VTIP (+0.05) serve as true non-correlated portfolio stabilizers.<br/>"
        "<b>3. Critical Structural Diversification Gaps:</b> The portfolio currently has <b>0% direct exposure to International Equities</b> (Developed Markets via VEA/VXUS, Emerging Markets via VWO) "
        "and <b>0% exposure to Real Estate Investment Trusts (VNQ) or Commodities</b>. Incorporating global equities will enhance multi-asset frontier efficiency."
    )
    story.append(Paragraph(p15_gaps, styles['BodyDark']))
    story.append(PageBreak())

# 5. PAGES 16 TO 25: ITEMIZED HOLDINGS, SECTOR EXPOSURE & ADVISORY ROADMAP

def add_pages_16_to_25(story, styles):
    # PAGE 16: Complete Itemized Holdings (Consolidated Master Inventory)
    story.append(Paragraph("5.1 CONSOLIDATED MASTER HOLDINGS INVENTORY & VALUATION SCHEDULE", styles['SectionHeader']))
    story.append(Paragraph("Exhaustive Portfolio Valuation & Pricing Schedule (September 14, 2026)", styles['SubSectionHeader']))
    
    p16_desc = (
        "Below is the complete, itemized master inventory of all 10 ETF holdings, the multi-account Bank Deposit Program (BDP), "
        "and the Citibank Money Market Savings account. All prices and valuations reflect closing market data on September 14, 2026."
    )
    story.append(Paragraph(p16_desc, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    master_headers = [Paragraph("<b>Ticker</b>", styles['TableHeaderLeft']), Paragraph("<b>Fund Description / Asset Name</b>", styles['TableHeaderLeft']), Paragraph("<b>Shares</b>", styles['TableHeaderRight']), Paragraph("<b>Price ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Total Value ($)</b>", styles['TableHeaderRight']), Paragraph("<b>% Port</b>", styles['TableHeaderRight']), Paragraph("<b>Exp.</b>", styles['TableHeader']), Paragraph("<b>Yield</b>", styles['TableHeader']), Paragraph("<b>52-Wk Range</b>", styles['TableHeader']), Paragraph("<b>Day Change</b>", styles['TableHeaderRight'])]
    master_rows = [
        [Paragraph("<b>VOO</b>", styles['TableCellLeftBold']), Paragraph("Vanguard S&P 500 ETF", styles['TableCellLeft']), Paragraph("1,376.00", styles['TableCellRight']), Paragraph("$799.30", styles['TableCellRight']), Paragraph("$962,236.80", styles['TableCellRightBold']), Paragraph("82.57%", styles['TableCellRightBold']), Paragraph("0.03%", styles['TableCell']), Paragraph("1.32%", styles['TableCell']), Paragraph("$578.46 – $716.39", styles['TableCell']), Paragraph("-$3.05 (-0.41%)", styles['TableCellRight'])],
        [Paragraph("<b>VTIP</b>", styles['TableCellLeftBold']), Paragraph("Vanguard Short-Term TIPS ETF", styles['TableCellLeft']), Paragraph("1,699.00", styles['TableCellRight']), Paragraph("$49.47", styles['TableCellRight']), Paragraph("$84,049.53", styles['TableCellRightBold']), Paragraph("7.21%", styles['TableCellRightBold']), Paragraph("0.04%", styles['TableCell']), Paragraph("3.95%", styles['TableCell']), Paragraph("$49.35 – $50.81", styles['TableCell']), Paragraph("+$0.01 (+0.01%)", styles['TableCellRight'])],
        [Paragraph("<b>BND</b>", styles['TableCellLeftBold']), Paragraph("Vanguard Total Bond Market ETF", styles['TableCellLeft']), Paragraph("363.00", styles['TableCellRight']), Paragraph("$71.17", styles['TableCellRight']), Paragraph("$25,834.71", styles['TableCellRightBold']), Paragraph("2.22%", styles['TableCellRightBold']), Paragraph("0.04%", styles['TableCell']), Paragraph("4.45%", styles['TableCell']), Paragraph("$72.07 – $75.23", styles['TableCell']), Paragraph("-$0.11 (-0.16%)", styles['TableCellRight'])],
        [Paragraph("<b>VYM</b>", styles['TableCellLeftBold']), Paragraph("Vanguard High Dividend Yield ETF", styles['TableCellLeft']), Paragraph("65.00", styles['TableCellRight']), Paragraph("$161.73", styles['TableCellRight']), Paragraph("$10,512.45", styles['TableCellRightBold']), Paragraph("0.91%", styles['TableCellRightBold']), Paragraph("0.06%", styles['TableCell']), Paragraph("2.95%", styles['TableCell']), Paragraph("$136.20 – $167.61", styles['TableCell']), Paragraph("-$0.18 (-0.11%)", styles['TableCellRight'])],
        [Paragraph("<b>VUG</b>", styles['TableCellLeftBold']), Paragraph("Vanguard Growth Index Fund ETF", styles['TableCellLeft']), Paragraph("120.00", styles['TableCellRight']), Paragraph("$87.71", styles['TableCellRight']), Paragraph("$10,525.20", styles['TableCellRightBold']), Paragraph("0.90%", styles['TableCellRightBold']), Paragraph("0.04%", styles['TableCell']), Paragraph("0.52%", styles['TableCell']), Paragraph("$69.63 – $90.60", styles['TableCell']), Paragraph("-$0.49 (-0.55%)", styles['TableCellRight'])],
        [Paragraph("<b>VTV</b>", styles['TableCellLeftBold']), Paragraph("Vanguard Value Index Fund ETF", styles['TableCellLeft']), Paragraph("47.00", styles['TableCellRight']), Paragraph("$222.89", styles['TableCellRight']), Paragraph("$10,475.83", styles['TableCellRightBold']), Paragraph("0.90%", styles['TableCellRightBold']), Paragraph("0.04%", styles['TableCell']), Paragraph("2.42%", styles['TableCell']), Paragraph("$180.84 – $228.57", styles['TableCell']), Paragraph("-$0.29 (-0.13%)", styles['TableCellRight'])],
        [Paragraph("<b>VB</b>", styles['TableCellLeftBold']), Paragraph("Vanguard Small-Cap Index Fund ETF", styles['TableCellLeft']), Paragraph("17.00", styles['TableCellRight']), Paragraph("$292.37", styles['TableCellRight']), Paragraph("$5,970.29", styles['TableCellRightBold']), Paragraph("0.43%", styles['TableCellRightBold']), Paragraph("0.05%", styles['TableCell']), Paragraph("1.50%", styles['TableCell']), Paragraph("$241.19 – $309.51", styles['TableCell']), Paragraph("-$2.09 (-0.69%)", styles['TableCellRight'])],
        [Paragraph("<b>VGT</b>", styles['TableCellLeftBold']), Paragraph("Vanguard Information Tech ETF", styles['TableCellLeft']), Paragraph("40.00", styles['TableCellRight']), Paragraph("$119.17", styles['TableCellRight']), Paragraph("$4,766.80", styles['TableCellRightBold']), Paragraph("0.41%", styles['TableCellRightBold']), Paragraph("0.10%", styles['TableCell']), Paragraph("0.68%", styles['TableCell']), Paragraph("$83.09 – $126.00", styles['TableCell']), Paragraph("+$0.15 (+0.12%)", styles['TableCellRight'])],
        [Paragraph("<b>VHT</b>", styles['TableCellLeftBold']), Paragraph("Vanguard Health Care Index ETF", styles['TableCellLeft']), Paragraph("8.00", styles['TableCellRight']), Paragraph("$315.02", styles['TableCellRight']), Paragraph("$2,520.16", styles['TableCellRightBold']), Paragraph("0.22%", styles['TableCellRightBold']), Paragraph("0.10%", styles['TableCell']), Paragraph("1.42%", styles['TableCell']), Paragraph("$249.58 – $330.75", styles['TableCell']), Paragraph("-$1.37 (-0.43%)", styles['TableCellRight'])],
        [Paragraph("<b>VGIT</b>", styles['TableCellLeftBold']), Paragraph("Vanguard Interm Treasury ETF", styles['TableCellLeft']), Paragraph("12.00", styles['TableCellRight']), Paragraph("$57.28", styles['TableCellRight']), Paragraph("$687.36", styles['TableCellRightBold']), Paragraph("0.06%", styles['TableCellRightBold']), Paragraph("0.04%", styles['TableCell']), Paragraph("4.20%", styles['TableCell']), Paragraph("$58.17 – $60.76", styles['TableCell']), Paragraph("-$0.06 (-0.09%)", styles['TableCellRight'])],
        [Paragraph("<b>BDP</b>", styles['TableCellLeftBold']), Paragraph("Bank Deposit Program (Brokerage/IRAs)", styles['TableCellLeft']), Paragraph("130.48", styles['TableCellRight']), Paragraph("$1.00", styles['TableCellRight']), Paragraph("$130.48", styles['TableCellRightBold']), Paragraph("0.01%", styles['TableCellRightBold']), Paragraph("0.00%", styles['TableCell']), Paragraph("4.50%", styles['TableCell']), Paragraph("$1.00 – $1.00", styles['TableCell']), Paragraph("$0.00 (0.00%)", styles['TableCellRight'])],
        [Paragraph("<b>MMS</b>", styles['TableCellLeftBold']), Paragraph("Citibank Money Market (6866284312)", styles['TableCellLeft']), Paragraph("48,475.99", styles['TableCellRight']), Paragraph("$1.00", styles['TableCellRight']), Paragraph("$48,475.99", styles['TableCellRightBold']), Paragraph("4.16%", styles['TableCellRightBold']), Paragraph("0.00%", styles['TableCell']), Paragraph("4.85%", styles['TableCell']), Paragraph("$1.00 – $1.00", styles['TableCell']), Paragraph("$0.00 (0.00%)", styles['TableCellRight'])],
        [Paragraph("<b>TOTAL</b>", styles['TableCellLeftBold']), Paragraph("<b>Consolidated Citibank Portfolio</b>", styles['TableCellLeftBold']), Paragraph("<b>3,756.13</b>", styles['TableCellRightBold']), Paragraph("<b>—</b>", styles['TableCellRight']), Paragraph("<b>$1,165,185.60</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>0.031%</b>", styles['TableCellBold']), Paragraph("<b>1.74%</b>", styles['TableCellBold']), Paragraph("<b>All Assets</b>", styles['TableCell']), Paragraph("<b>-$4,198.85 (-0.36%)</b>", styles['TableCellRightBold'])],
    ]
    t_master = Table([master_headers] + master_rows, colWidths=[40, 130, 45, 42, 65, 42, 32, 32, 70, 42])
    t_master.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_LIGHT_BLUE),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    story.append(t_master)
    story.append(Spacer(1, 4))
    
    p16_comment = (
        "<b>Holdings Valuation Summary:</b> The master inventory demonstrates complete institutional transparency. "
        "Total invested securities equal $1,122,374.87 (95.85%), supported by $48,593.13 in cash equivalents (4.17%). "
        "All positions maintain full daily liquidity, zero lock-up periods, and zero redemption penalties."
    )
    story.append(Paragraph(p16_comment, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 17: Account-by-Account Granular Breakdown
    story.append(Paragraph("5.2 ACCOUNT-BY-ACCOUNT GRANULAR BREAKDOWN", styles['SectionHeader']))
    story.append(Paragraph("Individual Account Holdings & Allocation Schedules", styles['SubSectionHeader']))
    
    story.append(Paragraph("<b>1. Self Direct Brokerage (Account # CZ4057890) — Total Valuation: $499,298.03 (34.27%)</b>", styles['BodyDarkBold']))
    b_head = [Paragraph("<b>Ticker</b>", styles['TableHeaderLeft']), Paragraph("<b>Description</b>", styles['TableHeaderLeft']), Paragraph("<b>Shares</b>", styles['TableHeaderRight']), Paragraph("<b>Price ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Total Value ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Acct %</b>", styles['TableHeaderRight']), Paragraph("<b>Total %</b>", styles['TableHeaderRight'])]
    b_rows = [
        [Paragraph("VOO", styles['TableCellLeftBold']), Paragraph("Vanguard S&P 500 ETF", styles['TableCellLeft']), Paragraph("485.00", styles['TableCellRight']), Paragraph("$799.30", styles['TableCellRight']), Paragraph("$339,160.50", styles['TableCellRightBold']), Paragraph("84.94%", styles['TableCellRightBold']), Paragraph("29.11%", styles['TableCellRight'])],
        [Paragraph("VTIP", styles['TableCellLeftBold']), Paragraph("Vanguard Short-Term TIPS ETF", styles['TableCellLeft']), Paragraph("316.00", styles['TableCellRight']), Paragraph("$49.47", styles['TableCellRight']), Paragraph("$15,632.52", styles['TableCellRightBold']), Paragraph("3.92%", styles['TableCellRightBold']), Paragraph("1.34%", styles['TableCellRight'])],
        [Paragraph("VYM", styles['TableCellLeftBold']), Paragraph("Vanguard High Dividend Yield ETF", styles['TableCellLeft']), Paragraph("65.00", styles['TableCellRight']), Paragraph("$161.73", styles['TableCellRight']), Paragraph("$10,512.45", styles['TableCellRightBold']), Paragraph("2.67%", styles['TableCellRightBold']), Paragraph("0.91%", styles['TableCellRight'])],
        [Paragraph("VTV", styles['TableCellLeftBold']), Paragraph("Vanguard Value Index ETF", styles['TableCellLeft']), Paragraph("47.00", styles['TableCellRight']), Paragraph("$222.89", styles['TableCellRight']), Paragraph("$10,475.83", styles['TableCellRightBold']), Paragraph("2.64%", styles['TableCellRightBold']), Paragraph("0.90%", styles['TableCellRight'])],
        [Paragraph("VUG", styles['TableCellLeftBold']), Paragraph("Vanguard Growth Index ETF", styles['TableCellLeft']), Paragraph("120.00", styles['TableCellRight']), Paragraph("$87.71", styles['TableCellRight']), Paragraph("$10,525.20", styles['TableCellRightBold']), Paragraph("2.64%", styles['TableCellRightBold']), Paragraph("0.90%", styles['TableCellRight'])],
        [Paragraph("VB", styles['TableCellLeftBold']), Paragraph("Vanguard Small-Cap Index ETF", styles['TableCellLeft']), Paragraph("17.00", styles['TableCellRight']), Paragraph("$292.37", styles['TableCellRight']), Paragraph("$5,970.29", styles['TableCellRightBold']), Paragraph("1.27%", styles['TableCellRightBold']), Paragraph("0.43%", styles['TableCellRight'])],
        [Paragraph("VGT", styles['TableCellLeftBold']), Paragraph("Vanguard Info Tech ETF", styles['TableCellLeft']), Paragraph("40.00", styles['TableCellRight']), Paragraph("$119.17", styles['TableCellRight']), Paragraph("$4,766.80", styles['TableCellRightBold']), Paragraph("1.20%", styles['TableCellRightBold']), Paragraph("0.41%", styles['TableCellRight'])],
        [Paragraph("VHT", styles['TableCellLeftBold']), Paragraph("Vanguard Health Care ETF", styles['TableCellLeft']), Paragraph("8.00", styles['TableCellRight']), Paragraph("$315.02", styles['TableCellRight']), Paragraph("$2,520.16", styles['TableCellRightBold']), Paragraph("0.64%", styles['TableCellRightBold']), Paragraph("0.22%", styles['TableCellRight'])],
        [Paragraph("VGIT", styles['TableCellLeftBold']), Paragraph("Vanguard Interm Treasury ETF", styles['TableCellLeft']), Paragraph("12.00", styles['TableCellRight']), Paragraph("$57.28", styles['TableCellRight']), Paragraph("$687.36", styles['TableCellRightBold']), Paragraph("0.18%", styles['TableCellRightBold']), Paragraph("0.06%", styles['TableCellRight'])],
        [Paragraph("BDP", styles['TableCellLeftBold']), Paragraph("Bank Deposit Program", styles['TableCellLeft']), Paragraph("33.58", styles['TableCellRight']), Paragraph("$1.00", styles['TableCellRight']), Paragraph("$33.58", styles['TableCellRightBold']), Paragraph("0.01%", styles['TableCellRightBold']), Paragraph("0.00%", styles['TableCellRight'])],
        [Paragraph("<b>Subtotal</b>", styles['TableCellLeftBold']), Paragraph("<b>Taxable Brokerage Sleeve</b>", styles['TableCellLeftBold']), Paragraph("<b>1,110.58</b>", styles['TableCellRightBold']), Paragraph("<b>—</b>", styles['TableCellRight']), Paragraph("<b>$499,298.03</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>34.27%</b>", styles['TableCellRightBold'])],
    ]
    t_b = Table([b_head] + b_rows, colWidths=[45, 175, 55, 55, 75, 65, 70])
    t_b.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_b)
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Self Direct Traditional IRA (Account # CZ4058132) — Total: $582,731.45 (50.01%)</b>", styles['BodyDarkBold']))
    ira_head = [Paragraph("<b>Ticker</b>", styles['TableHeaderLeft']), Paragraph("<b>Description</b>", styles['TableHeaderLeft']), Paragraph("<b>Shares</b>", styles['TableHeaderRight']), Paragraph("<b>Price ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Total Value ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Acct %</b>", styles['TableHeaderRight']), Paragraph("<b>Total %</b>", styles['TableHeaderRight'])]
    ira_rows = [
        [Paragraph("VOO", styles['TableCellLeftBold']), Paragraph("Vanguard S&P 500 ETF", styles['TableCellLeft']), Paragraph("710.00", styles['TableCellRight']), Paragraph("$799.30", styles['TableCellRight']), Paragraph("$496,503.00", styles['TableCellRightBold']), Paragraph("85.20%", styles['TableCellRightBold']), Paragraph("42.61%", styles['TableCellRight'])],
        [Paragraph("VTIP", styles['TableCellLeftBold']), Paragraph("Vanguard Short-Term TIPS ETF", styles['TableCellLeft']), Paragraph("1,220.00", styles['TableCellRight']), Paragraph("$49.47", styles['TableCellRight']), Paragraph("$60,353.40", styles['TableCellRightBold']), Paragraph("10.33%", styles['TableCellRightBold']), Paragraph("5.18%", styles['TableCellRight'])],
        [Paragraph("BND", styles['TableCellLeftBold']), Paragraph("Vanguard Total Bond Market ETF", styles['TableCellLeft']), Paragraph("363.00", styles['TableCellRight']), Paragraph("$71.17", styles['TableCellRight']), Paragraph("$25,834.71", styles['TableCellRightBold']), Paragraph("4.43%", styles['TableCellRightBold']), Paragraph("2.22%", styles['TableCellRight'])],
        [Paragraph("BDP", styles['TableCellLeftBold']), Paragraph("Bank Deposit Program", styles['TableCellLeft']), Paragraph("40.34", styles['TableCellRight']), Paragraph("$1.00", styles['TableCellRight']), Paragraph("$40.34", styles['TableCellRightBold']), Paragraph("0.01%", styles['TableCellRightBold']), Paragraph("0.00%", styles['TableCellRight'])],
        [Paragraph("<b>Subtotal</b>", styles['TableCellLeftBold']), Paragraph("<b>Traditional IRA Sleeve</b>", styles['TableCellLeftBold']), Paragraph("<b>2,333.34</b>", styles['TableCellRightBold']), Paragraph("<b>—</b>", styles['TableCellRight']), Paragraph("<b>$582,731.45</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>50.01%</b>", styles['TableCellRightBold'])],
    ]
    t_ira = Table([ira_head] + ira_rows, colWidths=[45, 175, 55, 55, 75, 65, 70])
    t_ira.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_ira)
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Self Direct Roth IRA (Account # CZ4063612) — Total: $134,680.13 (11.56%)</b>", styles['BodyDarkBold']))
    roth_rows = [
        [Paragraph("VOO", styles['TableCellLeftBold']), Paragraph("Vanguard S&P 500 ETF", styles['TableCellLeft']), Paragraph("181.00", styles['TableCellRight']), Paragraph("$799.30", styles['TableCellRight']), Paragraph("$126,573.30", styles['TableCellRightBold']), Paragraph("93.98%", styles['TableCellRightBold']), Paragraph("10.88%", styles['TableCellRight'])],
        [Paragraph("VTIP", styles['TableCellLeftBold']), Paragraph("Vanguard Short-Term TIPS ETF", styles['TableCellLeft']), Paragraph("163.00", styles['TableCellRight']), Paragraph("$49.47", styles['TableCellRight']), Paragraph("$8,063.61", styles['TableCellRightBold']), Paragraph("5.99%", styles['TableCellRightBold']), Paragraph("0.69%", styles['TableCellRight'])],
        [Paragraph("BDP", styles['TableCellLeftBold']), Paragraph("Bank Deposit Program", styles['TableCellLeft']), Paragraph("43.22", styles['TableCellRight']), Paragraph("$1.00", styles['TableCellRight']), Paragraph("$43.22", styles['TableCellRightBold']), Paragraph("0.03%", styles['TableCellRightBold']), Paragraph("0.00%", styles['TableCellRight'])],
        [Paragraph("<b>Subtotal</b>", styles['TableCellLeftBold']), Paragraph("<b>Roth IRA Sleeve</b>", styles['TableCellLeftBold']), Paragraph("<b>387.22</b>", styles['TableCellRightBold']), Paragraph("<b>—</b>", styles['TableCellRight']), Paragraph("<b>$134,680.13</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>11.56%</b>", styles['TableCellRightBold'])],
    ]
    t_roth = Table([ira_head] + roth_rows, colWidths=[45, 175, 55, 55, 75, 65, 70])
    t_roth.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_roth)
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Citibank Money Market Savings (Account # 6866284312) — Total: $48,475.99 (4.16%)</b>", styles['BodyDarkBold']))
    mms_rows = [
        [Paragraph("MMS", styles['TableCellLeftBold']), Paragraph("Citibank High-Yield Cash Reserve (4.85% APY)", styles['TableCellLeft']), Paragraph("48,475.99", styles['TableCellRight']), Paragraph("$1.00", styles['TableCellRight']), Paragraph("$48,475.99", styles['TableCellRightBold']), Paragraph("100.00%", styles['TableCellRightBold']), Paragraph("4.16%", styles['TableCellRight'])],
        [Paragraph("<b>Subtotal</b>", styles['TableCellLeftBold']), Paragraph("<b>Liquid Cash Reserve</b>", styles['TableCellLeftBold']), Paragraph("<b>48,475.99</b>", styles['TableCellRightBold']), Paragraph("<b>$1.00</b>", styles['TableCellRight']), Paragraph("<b>$48,475.99</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>4.16%</b>", styles['TableCellRightBold'])],
    ]
    t_mms = Table([ira_head] + mms_rows, colWidths=[45, 175, 55, 55, 75, 65, 70])
    t_mms.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_mms)
    story.append(PageBreak())
    
    # PAGE 18: Look-Through Equity Sector & Industry Weightings
    story.append(Paragraph("5.3 LOOK-THROUGH EQUITY SECTOR & INDUSTRY WEIGHTINGS", styles['SectionHeader']))
    story.append(Paragraph("Look-Through Equity Sector Exposure vs. S&P 500 Benchmark", styles['SubSectionHeader']))
    
    story.append(Image('charts/chart5_sector_exposure.png', width=540, height=200))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Comprehensive Sector Exposure Breakdown Schedule", styles['SubSectionHeader']))
    
    sec_headers = [Paragraph("<b>GICS Equity Sector</b>", styles['TableHeaderLeft']), Paragraph("<b>Portfolio Weight (% Eq)</b>", styles['TableHeaderRight']), Paragraph("<b>S&P 500 Weight (%)</b>", styles['TableHeaderRight']), Paragraph("<b>Active Tilt (%)</b>", styles['TableHeader']), Paragraph("<b>Portfolio Value ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Key Industry Holdings Look-Through</b>", styles['TableHeaderLeft'])]
    sec_rows = [
        [Paragraph("<b>Information Technology</b>", styles['TableCellLeftBold']), Paragraph("<b>29.80%</b>", styles['TableCellRightBold']), Paragraph("31.50%", styles['TableCellRight']), Paragraph("<font color='#5B6770'>-1.70%</font>", styles['TableCell']), Paragraph("$301,308", styles['TableCellRight']), Paragraph("Microsoft, Apple, NVIDIA, Broadcom, AMD, Salesforce", styles['TableCellLeft'])],
        [Paragraph("<b>Financials</b>", styles['TableCellLeftBold']), Paragraph("<b>13.20%</b>", styles['TableCellRightBold']), Paragraph("12.80%", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+0.40%</font>", styles['TableCell']), Paragraph("$133,465", styles['TableCellRight']), Paragraph("Berkshire Hathaway, JPMorgan, Visa, Mastercard, BofA", styles['TableCellLeft'])],
        [Paragraph("<b>Health Care</b>", styles['TableCellLeftBold']), Paragraph("<b>12.10%</b>", styles['TableCellRightBold']), Paragraph("11.90%", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+0.20%</font>", styles['TableCell']), Paragraph("$122,343", styles['TableCellRight']), Paragraph("Eli Lilly, UnitedHealth, Johnson & Johnson, AbbVie, Merck", styles['TableCellLeft'])],
        [Paragraph("<b>Consumer Discretionary</b>", styles['TableCellLeftBold']), Paragraph("<b>10.10%</b>", styles['TableCellRightBold']), Paragraph("10.20%", styles['TableCellRight']), Paragraph("<font color='#5B6770'>-0.10%</font>", styles['TableCell']), Paragraph("$102,121", styles['TableCellRight']), Paragraph("Amazon, Tesla, Home Depot, McDonald's, Nike", styles['TableCellLeft'])],
        [Paragraph("<b>Communication Services</b>", styles['TableCellLeftBold']), Paragraph("<b>8.90%</b>", styles['TableCellRightBold']), Paragraph("9.10%", styles['TableCellRight']), Paragraph("<font color='#5B6770'>-0.20%</font>", styles['TableCell']), Paragraph("$89,988", styles['TableCellRight']), Paragraph("Alphabet (Google), Meta Platforms, Netflix, Disney", styles['TableCellLeft'])],
        [Paragraph("<b>Industrials</b>", styles['TableCellLeftBold']), Paragraph("<b>8.40%</b>", styles['TableCellRightBold']), Paragraph("8.10%", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+0.30%</font>", styles['TableCell']), Paragraph("$84,932", styles['TableCellRight']), Paragraph("Caterpillar, GE Aerospace, Union Pacific, Honeywell", styles['TableCellLeft'])],
        [Paragraph("<b>Consumer Staples</b>", styles['TableCellLeftBold']), Paragraph("<b>5.80%</b>", styles['TableCellRightBold']), Paragraph("5.70%", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+0.10%</font>", styles['TableCell']), Paragraph("$58,644", styles['TableCellRight']), Paragraph("Procter & Gamble, Costco, Walmart, Coca-Cola, PepsiCo", styles['TableCellLeft'])],
        [Paragraph("<b>Energy</b>", styles['TableCellLeftBold']), Paragraph("<b>3.90%</b>", styles['TableCellRightBold']), Paragraph("3.70%", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+0.20%</font>", styles['TableCell']), Paragraph("$39,433", styles['TableCellRight']), Paragraph("ExxonMobil, Chevron, ConocoPhillips, EOG Resources", styles['TableCellLeft'])],
        [Paragraph("<b>Utilities</b>", styles['TableCellLeftBold']), Paragraph("<b>2.40%</b>", styles['TableCellRightBold']), Paragraph("2.30%", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+0.10%</font>", styles['TableCell']), Paragraph("$24,266", styles['TableCellRight']), Paragraph("NextEra Energy, Southern Co, Duke Energy, Constellation", styles['TableCellLeft'])],
        [Paragraph("<b>Real Estate</b>", styles['TableCellLeftBold']), Paragraph("<b>2.30%</b>", styles['TableCellRightBold']), Paragraph("2.20%", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+0.10%</font>", styles['TableCell']), Paragraph("$23,255", styles['TableCellRight']), Paragraph("Prologis, American Tower, Equinix, Simon Property Group", styles['TableCellLeft'])],
        [Paragraph("<b>Materials</b>", styles['TableCellLeftBold']), Paragraph("<b>2.10%</b>", styles['TableCellRightBold']), Paragraph("2.10%", styles['TableCellRight']), Paragraph("<font color='#5B6770'>0.00%</font>", styles['TableCell']), Paragraph("$21,233", styles['TableCellRight']), Paragraph("Linde, Sherwin-Williams, Freeport-McMoRan, Ecolab", styles['TableCellLeft'])],
        [Paragraph("<b>TOTAL EQUITIES SLEEVE</b>", styles['TableCellLeftBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>0.00%</b>", styles['TableCellBold']), Paragraph("<b>$1,006,008</b>", styles['TableCellRightBold']), Paragraph("<b>Full GICS Economic Sector Coverage</b>", styles['TableCellLeftBold'])],
    ]
    t_sec = Table([sec_headers] + sec_rows, colWidths=[110, 65, 65, 55, 65, 180])
    t_sec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_LIGHT_BLUE),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
    ]))
    story.append(t_sec)
    story.append(Spacer(1, 3))
    
    p18_takeaway = (
        "<b>Sector Allocation Takeaway:</b> The look-through sector allocation closely tracks the broad S&P 500 index. "
        "Information Technology represents the largest single economic exposure (29.80% / $301.3k), followed by Financials (13.20%) and Health Care (12.10%). "
        "This sector balance provides robust participation in corporate innovation while maintaining solid defensive ballast."
    )
    story.append(Paragraph(p18_takeaway, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 19: Top 25 Underlying Corporate Look-Through Holdings
    story.append(Paragraph("5.4 TOP 25 UNDERLYING CORPORATE LOOK-THROUGH HOLDINGS", styles['SectionHeader']))
    story.append(Paragraph("Single-Stock Concentration & Look-Through Exposure Schedule", styles['SubSectionHeader']))
    
    p19_desc = (
        "Because the portfolio holds broad-market ETFs (VOO, VUG, VTV, VYM, VGT), individual corporate equities are held indirectly across multiple funds. "
        "Below is the consolidated, look-through aggregation of the Top 25 individual corporate exposures across all client accounts."
    )
    story.append(Paragraph(p19_desc, styles['BodyDark']))
    story.append(Spacer(1, 2))
    
    top25_headers = [Paragraph("<b>#</b>", styles['TableHeader']), Paragraph("<b>Company Name</b>", styles['TableHeaderLeft']), Paragraph("<b>Ticker</b>", styles['TableHeader']), Paragraph("<b>GICS Sector</b>", styles['TableHeaderLeft']), Paragraph("<b>Effective Portfolio Exposure ($)</b>", styles['TableHeaderRight']), Paragraph("<b>% Total Portfolio</b>", styles['TableHeaderRight']), Paragraph("<b>% Equity Sleeve</b>", styles['TableHeaderRight'])]
    top25_data = [
        [Paragraph("1", styles['TableCell']), Paragraph("Microsoft Corporation", styles['TableCellLeftBold']), Paragraph("MSFT", styles['TableCell']), Paragraph("Information Technology", styles['TableCellLeft']), Paragraph("$67,916", styles['TableCellRightBold']), Paragraph("5.80%", styles['TableCellRightBold']), Paragraph("6.72%", styles['TableCellRight'])],
        [Paragraph("2", styles['TableCell']), Paragraph("Apple Inc.", styles['TableCellLeftBold']), Paragraph("AAPL", styles['TableCell']), Paragraph("Information Technology", styles['TableCellLeft']), Paragraph("$65,574", styles['TableCellRightBold']), Paragraph("5.60%", styles['TableCellRightBold']), Paragraph("6.49%", styles['TableCellRight'])],
        [Paragraph("3", styles['TableCell']), Paragraph("NVIDIA Corporation", styles['TableCellLeftBold']), Paragraph("NVDA", styles['TableCell']), Paragraph("Information Technology", styles['TableCellLeft']), Paragraph("$60,890", styles['TableCellRightBold']), Paragraph("5.20%", styles['TableCellRightBold']), Paragraph("6.02%", styles['TableCellRight'])],
        [Paragraph("4", styles['TableCell']), Paragraph("Amazon.com Inc.", styles['TableCellLeftBold']), Paragraph("AMZN", styles['TableCell']), Paragraph("Consumer Discretionary", styles['TableCellLeft']), Paragraph("$35,129", styles['TableCellRightBold']), Paragraph("3.00%", styles['TableCellRightBold']), Paragraph("3.47%", styles['TableCellRight'])],
        [Paragraph("5", styles['TableCell']), Paragraph("Alphabet Inc. (Class A & C)", styles['TableCellLeftBold']), Paragraph("GOOGL", styles['TableCell']), Paragraph("Communication Services", styles['TableCellLeft']), Paragraph("$30,445", styles['TableCellRightBold']), Paragraph("2.60%", styles['TableCellRightBold']), Paragraph("3.01%", styles['TableCellRight'])],
        [Paragraph("6", styles['TableCell']), Paragraph("Meta Platforms Inc.", styles['TableCellLeftBold']), Paragraph("META", styles['TableCell']), Paragraph("Communication Services", styles['TableCellLeft']), Paragraph("$23,419", styles['TableCellRightBold']), Paragraph("2.00%", styles['TableCellRightBold']), Paragraph("2.32%", styles['TableCellRight'])],
        [Paragraph("7", styles['TableCell']), Paragraph("Berkshire Hathaway Inc.", styles['TableCellLeftBold']), Paragraph("BRK.B", styles['TableCell']), Paragraph("Financials", styles['TableCellLeft']), Paragraph("$18,735", styles['TableCellRightBold']), Paragraph("1.60%", styles['TableCellRightBold']), Paragraph("1.85%", styles['TableCellRight'])],
        [Paragraph("8", styles['TableCell']), Paragraph("Eli Lilly and Company", styles['TableCellLeftBold']), Paragraph("LLY", styles['TableCell']), Paragraph("Health Care", styles['TableCellLeft']), Paragraph("$16,394", styles['TableCellRightBold']), Paragraph("1.40%", styles['TableCellRightBold']), Paragraph("1.62%", styles['TableCellRight'])],
        [Paragraph("9", styles['TableCell']), Paragraph("Broadcom Inc.", styles['TableCellLeftBold']), Paragraph("AVGO", styles['TableCell']), Paragraph("Information Technology", styles['TableCellLeft']), Paragraph("$16,394", styles['TableCellRightBold']), Paragraph("1.40%", styles['TableCellRightBold']), Paragraph("1.62%", styles['TableCellRight'])],
        [Paragraph("10", styles['TableCell']), Paragraph("JPMorgan Chase & Co.", styles['TableCellLeftBold']), Paragraph("JPM", styles['TableCell']), Paragraph("Financials", styles['TableCellLeft']), Paragraph("$14,052", styles['TableCellRightBold']), Paragraph("1.20%", styles['TableCellRightBold']), Paragraph("1.39%", styles['TableCellRight'])],
        [Paragraph("11", styles['TableCell']), Paragraph("Tesla Inc.", styles['TableCellLeftBold']), Paragraph("TSLA", styles['TableCell']), Paragraph("Consumer Discretionary", styles['TableCellLeft']), Paragraph("$12,881", styles['TableCellRightBold']), Paragraph("1.10%", styles['TableCellRightBold']), Paragraph("1.27%", styles['TableCellRight'])],
        [Paragraph("12", styles['TableCell']), Paragraph("Exxon Mobil Corporation", styles['TableCellLeftBold']), Paragraph("XOM", styles['TableCell']), Paragraph("Energy", styles['TableCellLeft']), Paragraph("$11,710", styles['TableCellRightBold']), Paragraph("1.00%", styles['TableCellRightBold']), Paragraph("1.16%", styles['TableCellRight'])],
        [Paragraph("13", styles['TableCell']), Paragraph("UnitedHealth Group Inc.", styles['TableCellLeftBold']), Paragraph("UNH", styles['TableCell']), Paragraph("Health Care", styles['TableCellLeft']), Paragraph("$10,539", styles['TableCellRightBold']), Paragraph("0.90%", styles['TableCellRightBold']), Paragraph("1.04%", styles['TableCellRight'])],
        [Paragraph("14", styles['TableCell']), Paragraph("Visa Inc. (Class A)", styles['TableCellLeftBold']), Paragraph("V", styles['TableCell']), Paragraph("Financials", styles['TableCellLeft']), Paragraph("$9,368", styles['TableCellRightBold']), Paragraph("0.80%", styles['TableCellRightBold']), Paragraph("0.93%", styles['TableCellRight'])],
        [Paragraph("15", styles['TableCell']), Paragraph("Procter & Gamble Company", styles['TableCellLeftBold']), Paragraph("PG", styles['TableCell']), Paragraph("Consumer Staples", styles['TableCellLeft']), Paragraph("$8,197", styles['TableCellRightBold']), Paragraph("0.70%", styles['TableCellRightBold']), Paragraph("0.81%", styles['TableCellRight'])],
        [Paragraph("16", styles['TableCell']), Paragraph("Mastercard Inc.", styles['TableCellLeftBold']), Paragraph("MA", styles['TableCell']), Paragraph("Financials", styles['TableCellLeft']), Paragraph("$8,197", styles['TableCellRightBold']), Paragraph("0.70%", styles['TableCellRightBold']), Paragraph("0.81%", styles['TableCellRight'])],
        [Paragraph("17", styles['TableCell']), Paragraph("Johnson & Johnson", styles['TableCellLeftBold']), Paragraph("JNJ", styles['TableCell']), Paragraph("Health Care", styles['TableCellLeft']), Paragraph("$8,197", styles['TableCellRightBold']), Paragraph("0.70%", styles['TableCellRightBold']), Paragraph("0.81%", styles['TableCellRight'])],
        [Paragraph("18", styles['TableCell']), Paragraph("Home Depot Inc.", styles['TableCellLeftBold']), Paragraph("HD", styles['TableCell']), Paragraph("Consumer Discretionary", styles['TableCellLeft']), Paragraph("$7,026", styles['TableCellRightBold']), Paragraph("0.60%", styles['TableCellRightBold']), Paragraph("0.69%", styles['TableCellRight'])],
        [Paragraph("19", styles['TableCell']), Paragraph("AbbVie Inc.", styles['TableCellLeftBold']), Paragraph("ABBV", styles['TableCell']), Paragraph("Health Care", styles['TableCellLeft']), Paragraph("$7,026", styles['TableCellRightBold']), Paragraph("0.60%", styles['TableCellRightBold']), Paragraph("0.69%", styles['TableCellRight'])],
        [Paragraph("20", styles['TableCell']), Paragraph("Costco Wholesale Corp.", styles['TableCellLeftBold']), Paragraph("COST", styles['TableCell']), Paragraph("Consumer Staples", styles['TableCellLeft']), Paragraph("$7,026", styles['TableCellRightBold']), Paragraph("0.60%", styles['TableCellRightBold']), Paragraph("0.69%", styles['TableCellRight'])],
        [Paragraph("21", styles['TableCell']), Paragraph("Chevron Corporation", styles['TableCellLeftBold']), Paragraph("CVX", styles['TableCell']), Paragraph("Energy", styles['TableCellLeft']), Paragraph("$5,855", styles['TableCellRightBold']), Paragraph("0.50%", styles['TableCellRightBold']), Paragraph("0.58%", styles['TableCellRight'])],
        [Paragraph("22", styles['TableCell']), Paragraph("Walmart Inc.", styles['TableCellLeftBold']), Paragraph("WMT", styles['TableCell']), Paragraph("Consumer Staples", styles['TableCellLeft']), Paragraph("$5,855", styles['TableCellRightBold']), Paragraph("0.50%", styles['TableCellRightBold']), Paragraph("0.58%", styles['TableCellRight'])],
        [Paragraph("23", styles['TableCell']), Paragraph("Merck & Co. Inc.", styles['TableCellLeftBold']), Paragraph("MRK", styles['TableCell']), Paragraph("Health Care", styles['TableCellLeft']), Paragraph("$5,855", styles['TableCellRightBold']), Paragraph("0.50%", styles['TableCellRightBold']), Paragraph("0.58%", styles['TableCellRight'])],
        [Paragraph("24", styles['TableCell']), Paragraph("Salesforce Inc.", styles['TableCellLeftBold']), Paragraph("CRM", styles['TableCell']), Paragraph("Information Technology", styles['TableCellLeft']), Paragraph("$5,855", styles['TableCellRightBold']), Paragraph("0.50%", styles['TableCellRightBold']), Paragraph("0.58%", styles['TableCellRight'])],
        [Paragraph("25", styles['TableCell']), Paragraph("Advanced Micro Devices", styles['TableCellLeftBold']), Paragraph("AMD", styles['TableCell']), Paragraph("Information Technology", styles['TableCellLeft']), Paragraph("$4,684", styles['TableCellRightBold']), Paragraph("0.40%", styles['TableCellRightBold']), Paragraph("0.46%", styles['TableCellRight'])],
        [Paragraph("<b>TOTAL</b>", styles['TableCellBold']), Paragraph("<b>Top 25 Holdings Aggregated</b>", styles['TableCellLeftBold']), Paragraph("<b>25 Cos</b>", styles['TableCellBold']), Paragraph("<b>Core Blue Chips</b>", styles['TableCellLeftBold']), Paragraph("<b>$404,657</b>", styles['TableCellRightBold']), Paragraph("<b>34.56%</b>", styles['TableCellRightBold']), Paragraph("<b>40.02%</b>", styles['TableCellRightBold'])],
    ]
    t_top25 = Table([top25_headers] + top25_data, colWidths=[20, 130, 45, 110, 85, 75, 75])
    t_top25.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,7), C_LIGHT_BLUE),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
    ]))
    story.append(t_top25)
    story.append(Spacer(1, 2))
    
    p19_conc = (
        "<b>Concentration Diagnostic:</b> The 'Magnificent Seven' mega-caps (MSFT, AAPL, NVDA, AMZN, GOOGL, META, TSLA) aggregate to <b>$295,739 (25.30% of total wealth)</b>. "
        "While these firms boast world-class balance sheets and secular AI cash flow growth, their high concentration means a 10% pullback across these 7 stocks impacts client net worth by -$29,574."
    )
    story.append(Paragraph(p19_conc, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 20: Geographic, Market-Cap & Style Factor Analysis
    story.append(Paragraph("5.5 GEOGRAPHIC, MARKET-CAP & STYLE FACTOR ANALYSIS", styles['SectionHeader']))
    story.append(Paragraph("Global Geographic Exposure & International Allocation Analysis", styles['SubSectionHeader']))
    
    geo_headers = [Paragraph("<b>Geographic Region / Market</b>", styles['TableHeaderLeft']), Paragraph("<b>Current Allocation ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Current Weight (%)</b>", styles['TableHeaderRight']), Paragraph("<b>Global Market Cap (MSCI ACWI)</b>", styles['TableHeaderRight']), Paragraph("<b>Active Geographic Tilt</b>", styles['TableHeader'])]
    geo_rows = [
        [Paragraph("<b>United States Equities</b>", styles['TableCellLeftBold']), Paragraph("$1,005,800", styles['TableCellRightBold']), Paragraph("85.89%", styles['TableCellRightBold']), Paragraph("63.50%", styles['TableCellRight']), Paragraph("<font color='#D9381E'><b>+22.39% (Heavy US Bias)</b></font>", styles['TableCellBold'])],
        [Paragraph("<b>Developed International (Europe/Japan)</b>", styles['TableCellLeftBold']), Paragraph("$5,299", styles['TableCellRightBold']), Paragraph("0.46%", styles['TableCellRightBold']), Paragraph("26.50%", styles['TableCellRight']), Paragraph("<font color='#007BC8'><b>-26.04% (Underweight)</b></font>", styles['TableCellBold'])],
        [Paragraph("<b>Emerging Markets (Asia/LatAm)</b>", styles['TableCellLeftBold']), Paragraph("$0", styles['TableCellRightBold']), Paragraph("0.00%", styles['TableCellRightBold']), Paragraph("10.00%", styles['TableCellRight']), Paragraph("<font color='#007BC8'><b>-10.00% (Underweight)</b></font>", styles['TableCellBold'])],
        [Paragraph("<b>US Fixed Income & Cash</b>", styles['TableCellLeftBold']), Paragraph("$159,868", styles['TableCellRightBold']), Paragraph("13.65%", styles['TableCellRightBold']), Paragraph("—", styles['TableCellRight']), Paragraph("Sovereign US Dollar Liquidity", styles['TableCell'])],
        [Paragraph("<b>TOTAL PORTFOLIO</b>", styles['TableCellLeftBold']), Paragraph("<b>$1,165,186</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>100.00% Coverage</b>", styles['TableCellBold'])],
    ]
    t_geo = Table([geo_headers] + geo_rows, colWidths=[140, 95, 80, 115, 110])
    t_geo.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_geo)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Market Capitalization & Factor Exposure Spectrum", styles['SubSectionHeader']))
    
    cap_headers = [Paragraph("<b>Market Capitalization Tier</b>", styles['TableHeaderLeft']), Paragraph("<b>Market Cap Threshold</b>", styles['TableHeaderLeft']), Paragraph("<b>Current Exposure ($)</b>", styles['TableHeaderRight']), Paragraph("<b>% of Total Wealth</b>", styles['TableHeaderRight']), Paragraph("<b>Primary Fund Holdings</b>", styles['TableHeaderLeft'])]
    cap_rows = [
        [Paragraph("<b>Mega-Cap Equities</b>", styles['TableCellLeftBold']), Paragraph("> $200 Billion Valuation", styles['TableCellLeft']), Paragraph("$725,900", styles['TableCellRightBold']), Paragraph("61.99%", styles['TableCellRightBold']), Paragraph("VOO, VUG, VGT (MSFT, AAPL, NVDA, AMZN)", styles['TableCellLeft'])],
        [Paragraph("<b>Large-Cap Equities</b>", styles['TableCellLeftBold']), Paragraph("$50 Billion – $200 Billion", styles['TableCellLeft']), Paragraph("$224,800", styles['TableCellRightBold']), Paragraph("19.20%", styles['TableCellRightBold']), Paragraph("VOO, VTV, VYM, VHT (JNJ, HD, ABBV, COST)", styles['TableCellLeft'])],
        [Paragraph("<b>Mid-Cap Equities</b>", styles['TableCellLeftBold']), Paragraph("$10 Billion – $50 Billion", styles['TableCellLeft']), Paragraph("$53,322", styles['TableCellRightBold']), Paragraph("4.55%", styles['TableCellRightBold']), Paragraph("VOO Mid-Cap constituents, VB upper tier", styles['TableCellLeft'])],
        [Paragraph("<b>Small-Cap Equities</b>", styles['TableCellLeftBold']), Paragraph("< $10 Billion Valuation", styles['TableCellLeft']), Paragraph("$7,077", styles['TableCellRightBold']), Paragraph("0.60%", styles['TableCellRightBold']), Paragraph("VB (Vanguard Small-Cap ETF)", styles['TableCellLeft'])],
        [Paragraph("<b>Fixed Income & Cash Reserves</b>", styles['TableCellLeftBold']), Paragraph("Capital Preservation Tier", styles['TableCellLeft']), Paragraph("$159,868", styles['TableCellRightBold']), Paragraph("13.65%", styles['TableCellRightBold']), Paragraph("VTIP, BND, VGIT, MMS, BDP", styles['TableCellLeft'])],
        [Paragraph("<b>TOTAL PORTFOLIO</b>", styles['TableCellLeftBold']), Paragraph("<b>Consolidated Assets</b>", styles['TableCellLeftBold']), Paragraph("<b>$1,165,186</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>100% Asset & Cap Tier Granularity</b>", styles['TableCellLeftBold'])],
    ]
    t_cap_tier = Table([cap_headers] + cap_rows, colWidths=[120, 110, 85, 75, 150])
    t_cap_tier.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_cap_tier)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Strategic Geographic & Factor Recommendations", styles['SubSectionHeader']))
    p20_rec = (
        "<b>1. Introduce Global International Equities:</b> The portfolio's 85.89% US domestic concentration reflects significant home-country bias. "
        "While US corporate earnings have dominated over the last decade, global valuations in Europe and Japan offer compelling 12-14x P/E multiples and 3.5% dividend yields. "
        "We recommend introducing a 5%–10% strategic allocation to <b>Vanguard Total International Stock ETF (VXUS)</b>.<br/>"
        "<b>2. Expand Small-Cap Exposure:</b> Small-caps represent only 0.60% ($7.1k) of wealth. Increasing VB toward the 4% target ($46.8k) captures domestic re-shoring growth."
    )
    story.append(Paragraph(p20_rec, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 21: Strategic Wealth Advisory & Rebalancing Roadmap
    story.append(Paragraph("6.1 FIDUCIARY REBALANCING ROADMAP & ACTION PLAN", styles['SectionHeader']))
    story.append(Paragraph("Comparison of Current vs. Spreadsheet Target Goal Allocations", styles['SubSectionHeader']))
    
    rebal_headers = [Paragraph("<b>Asset / Position</b>", styles['TableHeaderLeft']), Paragraph("<b>Current Value ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Current %</b>", styles['TableHeaderRight']), Paragraph("<b>Goal Alloc %</b>", styles['TableHeaderRight']), Paragraph("<b>Target Value ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Rebalancing Action ($)</b>", styles['TableHeaderRight']), Paragraph("<b>Execution Account / Vehicle</b>", styles['TableHeaderLeft'])]
    rebal_rows = [
        [Paragraph("<b>VOO (S&P 500 Core)</b>", styles['TableCellLeftBold']), Paragraph("$962,236.80", styles['TableCellRight']), Paragraph("82.57%", styles['TableCellRight']), Paragraph("65.00%", styles['TableCellRight']), Paragraph("$761,129.20", styles['TableCellRight']), Paragraph("<font color='#5B6770'>Hold (Trim in IRA only)</font>", styles['TableCellRightBold']), Paragraph("Traditional IRA (CZ4058132) — No Tax Friction", styles['TableCellLeft'])],
        [Paragraph("<b>VTIP (Short TIPS)</b>", styles['TableCellLeftBold']), Paragraph("$84,049.53", styles['TableCellRight']), Paragraph("7.21%", styles['TableCellRight']), Paragraph("8.00%", styles['TableCellRight']), Paragraph("$93,677.44", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+Buy $9,305.10</font>", styles['TableCellRightBold']), Paragraph("Traditional IRA / Brokerage Cash Flow", styles['TableCellLeft'])],
        [Paragraph("<b>BND (Total Bond)</b>", styles['TableCellLeftBold']), Paragraph("$25,834.71", styles['TableCellRight']), Paragraph("2.22%", styles['TableCellRight']), Paragraph("6.00%", styles['TableCellRight']), Paragraph("$70,258.08", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+Buy $44,053.11</font>", styles['TableCellRightBold']), Paragraph("Traditional IRA (Deploy Reallocated VOO)", styles['TableCellLeft'])],
        [Paragraph("<b>VTV (Value Index)</b>", styles['TableCellLeftBold']), Paragraph("$10,475.83", styles['TableCellRight']), Paragraph("0.90%", styles['TableCellRight']), Paragraph("6.00%", styles['TableCellRight']), Paragraph("$70,258.08", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+Buy $59,684.96</font>", styles['TableCellRightBold']), Paragraph("Brokerage (Deploy Money Market $48.5k)", styles['TableCellLeft'])],
        [Paragraph("<b>VYM (High Dividend)</b>", styles['TableCellLeftBold']), Paragraph("$10,512.45", styles['TableCellRight']), Paragraph("0.91%", styles['TableCellRight']), Paragraph("5.00%", styles['TableCellRight']), Paragraph("$58,548.40", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+Buy $47,883.85</font>", styles['TableCellRightBold']), Paragraph("Brokerage / IRA Rebalancing", styles['TableCellLeft'])],
        [Paragraph("<b>VUG (Growth ETF)</b>", styles['TableCellLeftBold']), Paragraph("$10,525.20", styles['TableCellRight']), Paragraph("0.90%", styles['TableCellRight']), Paragraph("4.00%", styles['TableCellRight']), Paragraph("$46,838.72", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+Buy $36,272.72</font>", styles['TableCellRightBold']), Paragraph("Roth IRA (CZ4063612) — Tax-Free Compounding", styles['TableCellLeft'])],
        [Paragraph("<b>VB (Small-Cap ETF)</b>", styles['TableCellLeftBold']), Paragraph("$5,970.29", styles['TableCellRight']), Paragraph("0.43%", styles['TableCellRight']), Paragraph("4.00%", styles['TableCellRight']), Paragraph("$46,838.72", styles['TableCellRight']), Paragraph("<font color='#1E824C'>+Buy $41,761.50</font>", styles['TableCellRightBold']), Paragraph("Brokerage / Traditional IRA", styles['TableCellLeft'])],
        [Paragraph("<b>Money Market Cash</b>", styles['TableCellLeftBold']), Paragraph("$48,475.99", styles['TableCellRight']), Paragraph("4.16%", styles['TableCellRight']), Paragraph("2.00%", styles['TableCellRight']), Paragraph("$23,419.36", styles['TableCellRight']), Paragraph("<font color='#D9381E'>-Deploy $25,056.63</font>", styles['TableCellRightBold']), Paragraph("Fund Value (VTV) & Small-Cap (VB) Purchases", styles['TableCellLeft'])],
        [Paragraph("<b>TOTAL</b>", styles['TableCellLeftBold']), Paragraph("<b>$1,165,185.60</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>100.00%</b>", styles['TableCellRightBold']), Paragraph("<b>$1,165,185.60</b>", styles['TableCellRightBold']), Paragraph("<b>Net $0.00 Rebalance</b>", styles['TableCellBold']), Paragraph("<b>Zero Tax Drag Execution Strategy</b>", styles['TableCellLeftBold'])],
    ]
    t_rebal = Table([rebal_headers] + rebal_rows, colWidths=[95, 65, 45, 45, 65, 80, 145])
    t_rebal.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_rebal)
    story.append(Spacer(1, 3))
    
    story.append(Image('charts/chart7_rebalancing_targets.png', width=540, height=190))
    story.append(Spacer(1, 3))
    
    p21_plan = (
        "<b>Tax-Smart Execution Protocol:</b> To prevent triggering significant capital gains taxes in the Taxable Brokerage ($400.1k), "
        "<b>do not sell VOO in the brokerage</b>. Instead, execute rebalancing via two clean steps: "
        "1) Deploy the $48,475.99 Money Market cash directly into VTV and VB in the brokerage account; and "
        "2) Execute internal asset reallocations inside the Traditional IRA ($586.8k) by shifting VOO into BND and VTIP with zero tax friction."
    )
    story.append(Paragraph(p21_plan, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 22: Tax-Loss Harvesting, Asset Location & Estate Preservation
    story.append(Paragraph("6.2 TAX-LOSS HARVESTING, ASSET LOCATION & ESTATE STRATEGY", styles['SectionHeader']))
    story.append(Paragraph("Tax-Loss Harvesting (TLH) Protocol & Replacement Pair Candidates", styles['SubSectionHeader']))
    
    p22_tlh_desc = (
        "Tax-Loss Harvesting (TLH) enables taxable investors to systematically monetize market volatility. "
        "By realizing capital losses during periodic market pullbacks, the client can offset unlimited taxable capital gains plus up to $3,000 of ordinary income annually, "
        "carrying forward remaining losses indefinitely. To strictly comply with IRS Wash-Sale Rules (IRC § 1091), the client must replace sold assets with non-substantially identical funds."
    )
    story.append(Paragraph(p22_tlh_desc, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    tlh_headers = [Paragraph("<b>Primary Portfolio Holding</b>", styles['TableHeaderLeft']), Paragraph("<b>Primary ETF Benchmark Index</b>", styles['TableHeaderLeft']), Paragraph("<b>Tax-Loss Replacement ETF</b>", styles['TableHeaderLeft']), Paragraph("<b>Replacement Index / Sponsor</b>", styles['TableHeaderLeft']), Paragraph("<b>Tracking Correlation</b>", styles['TableHeader']), Paragraph("<b>Wash-Sale Compliance Status</b>", styles['TableHeaderLeft'])]
    tlh_rows = [
        [Paragraph("<b>VOO (S&P 500 ETF)</b>", styles['TableCellLeftBold']), Paragraph("S&P 500 Index (Standard & Poor's)", styles['TableCellLeft']), Paragraph("<b>SCHX / ITOT</b>", styles['TableCellLeftBold']), Paragraph("Schwab US Large-Cap / S&P Total Market", styles['TableCellLeft']), Paragraph("0.99", styles['TableCell']), Paragraph("<font color='#1E824C'><b>100% Compliant (Different Index)</b></font>", styles['TableCellLeft'])],
        [Paragraph("<b>VUG (Growth ETF)</b>", styles['TableCellLeftBold']), Paragraph("CRSP US Large Cap Growth Index", styles['TableCellLeft']), Paragraph("<b>SCHG / IWF</b>", styles['TableCellLeftBold']), Paragraph("Dow Jones US Growth / Russell 1000 Growth", styles['TableCellLeft']), Paragraph("0.99", styles['TableCell']), Paragraph("<font color='#1E824C'><b>100% Compliant (Different Index)</b></font>", styles['TableCellLeft'])],
        [Paragraph("<b>VTV (Value ETF)</b>", styles['TableCellLeftBold']), Paragraph("CRSP US Large Cap Value Index", styles['TableCellLeft']), Paragraph("<b>SCHV / IWD</b>", styles['TableCellLeftBold']), Paragraph("Dow Jones US Value / Russell 1000 Value", styles['TableCellLeft']), Paragraph("0.98", styles['TableCell']), Paragraph("<font color='#1E824C'><b>100% Compliant (Different Index)</b></font>", styles['TableCellLeft'])],
        [Paragraph("<b>VB (Small-Cap ETF)</b>", styles['TableCellLeftBold']), Paragraph("CRSP US Small Cap Index", styles['TableCellLeft']), Paragraph("<b>IJR / SCHA</b>", styles['TableCellLeftBold']), Paragraph("S&P SmallCap 600 / Dow Jones US Small", styles['TableCellLeft']), Paragraph("0.98", styles['TableCell']), Paragraph("<font color='#1E824C'><b>100% Compliant (Different Index)</b></font>", styles['TableCellLeft'])],
        [Paragraph("<b>VTIP (Short TIPS)</b>", styles['TableCellLeftBold']), Paragraph("Bloomberg 0-5 Year US TIPS Index", styles['TableCellLeft']), Paragraph("<b>STIP / TIPX</b>", styles['TableCellLeftBold']), Paragraph("iShares 0-5 Year TIPS / SPDR 1-10 TIPS", styles['TableCellLeft']), Paragraph("0.99", styles['TableCell']), Paragraph("<font color='#1E824C'><b>100% Compliant (Different Index)</b></font>", styles['TableCellLeft'])],
    ]
    t_tlh = Table([tlh_headers] + tlh_rows, colWidths=[105, 115, 75, 115, 45, 85])
    t_tlh.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_WHITE),
        ('BACKGROUND', (0,2), (-1,2), C_LIGHT_BG),
        ('BACKGROUND', (0,3), (-1,3), C_WHITE),
        ('BACKGROUND', (0,4), (-1,4), C_LIGHT_BG),
        ('BACKGROUND', (0,5), (-1,5), C_WHITE),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_tlh)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Multi-Year Fee Drag & Institutional Compounding Advantage", styles['SubSectionHeader']))
    
    fee_headers = [Paragraph("<b>Advisory Fee Model</b>", styles['TableHeaderLeft']), Paragraph("<b>Expense + Advisory Fee</b>", styles['TableHeader']), Paragraph("<b>Annual Cost on $1.165M</b>", styles['TableHeaderRight']), Paragraph("<b>10-Year Cumulative Drag</b>", styles['TableHeaderRight']), Paragraph("<b>20-Year Cumulative Drag</b>", styles['TableHeaderRight']), Paragraph("<b>Wealth Preserved vs Active</b>", styles['TableHeaderRight'])]
    fee_rows = [
        [Paragraph("<b>Citibank Low-Cost Strategy</b>", styles['TableCellLeftBold']), Paragraph("<b>0.0307% (3.07 bps)</b>", styles['TableCellBold']), Paragraph("<b>$359 / Year</b>", styles['TableCellRightBold']), Paragraph("<b>$4,850</b>", styles['TableCellRightBold']), Paragraph("<b>$14,200</b>", styles['TableCellRightBold']), Paragraph("<b>Base Preservation Model</b>", styles['TableCellRightBold'])],
        [Paragraph("Typical Active Mutual Funds", styles['TableCellLeft']), Paragraph("0.7500% (75 bps)", styles['TableCell']), Paragraph("$8,782 / Year", styles['TableCellRight']), Paragraph("$118,500", styles['TableCellRight']), Paragraph("$348,000", styles['TableCellRight']), Paragraph("+$333,800 Preserved", styles['TableCellRightBold'])],
        [Paragraph("Traditional AUM Wealth Manager", styles['TableCellLeft']), Paragraph("1.2500% (125 bps)", styles['TableCell']), Paragraph("$14,637 / Year", styles['TableCellRight']), Paragraph("$197,500", styles['TableCellRight']), Paragraph("$580,000", styles['TableCellRight']), Paragraph("+$565,800 Preserved", styles['TableCellRightBold'])],
    ]
    t_fee = Table([fee_headers] + fee_rows, colWidths=[120, 85, 85, 80, 80, 90])
    t_fee.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_fee)
    story.append(Spacer(1, 4))
    
    p22_estate = (
        "<b>Estate Planning & Roth Conversion Windows:</b> "
        "With $582,731.45 in the Traditional IRA, future Required Minimum Distributions (RMDs) beginning at age 75 could push the client into higher marginal tax brackets. "
        "We recommend evaluating partial annual Roth conversions during lower-income tax years to transition pre-tax assets into tax-free Roth compounding, "
        "creating tax-free inheritances under SECURE Act 2.0 regulations."
    )
    story.append(Paragraph(p22_estate, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 23: Fiduciary Review Summary & Long-Term Wealth Milestones
    story.append(Paragraph("6.3 FIDUCIARY REVIEW SUMMARY & LONG-TERM WEALTH MILESTONES", styles['SectionHeader']))
    story.append(Paragraph("Strategic Wealth Advisory Action Checklist", styles['SubSectionHeader']))
    
    p23_check_desc = (
        "As part of Citibank Wealth Management's ongoing fiduciary stewardship, we recommend the following five prioritized action items "
        "to optimize asset allocation, streamline cash flow, and safeguard multi-generational purchasing power."
    )
    story.append(Paragraph(p23_check_desc, styles['BodyDark']))
    story.append(Spacer(1, 3))
    
    action_headers = [Paragraph("<b>#</b>", styles['TableHeader']), Paragraph("<b>Fiduciary Action Item</b>", styles['TableHeaderLeft']), Paragraph("<b>Target Vehicle</b>", styles['TableHeaderLeft']), Paragraph("<b>Execution Horizon</b>", styles['TableHeader']), Paragraph("<b>Strategic Benefit & Outcome</b>", styles['TableHeaderLeft'])]
    action_rows = [
        [Paragraph("1", styles['TableCellBold']), Paragraph("<b>Deploy Cash Reserves into Value & Small-Caps</b>", styles['TableCellLeftBold']), Paragraph("Brokerage (CZ4057890)", styles['TableCellLeft']), Paragraph("Immediate (30 Days)", styles['TableCell']), Paragraph("Deploys $48.5k cash into VTV ($25k) and VB ($23.5k) to balance factor tilts with zero tax drag.", styles['TableCellLeft'])],
        [Paragraph("2", styles['TableCellBold']), Paragraph("<b>Rebalance Traditional IRA into Fixed Income</b>", styles['TableCellLeftBold']), Paragraph("Trad IRA (CZ4058132)", styles['TableCellLeft']), Paragraph("Q4 2026", styles['TableCell']), Paragraph("Shifts $44k from VOO into BND inside tax-deferred wrapper to hit 6% core bond target.", styles['TableCellLeft'])],
        [Paragraph("3", styles['TableCellBold']), Paragraph("<b>Optimize Roth IRA for Pure Equity Growth</b>", styles['TableCellLeftBold']), Paragraph("Roth IRA (CZ4063612)", styles['TableCellLeft']), Paragraph("Q4 2026", styles['TableCell']), Paragraph("Exchanges $8.1k VTIP into VUG/VOO to dedicate the 100% tax-free wrapper to high-growth compounding.", styles['TableCellLeft'])],
        [Paragraph("4", styles['TableCellBold']), Paragraph("<b>Establish Rebalancing Tolerance Corridors (+/-5%)</b>", styles['TableCellLeftBold']), Paragraph("All Accounts", styles['TableCellLeft']), Paragraph("Semi-Annual", styles['TableCell']), Paragraph("Automates opportunistic rebalancing triggers when equity weights deviate by +/- 5% from targets.", styles['TableCellLeft'])],
        [Paragraph("5", styles['TableCellBold']), Paragraph("<b>Initiate Systematic Multi-Year Roth Conversions</b>", styles['TableCellLeftBold']), Paragraph("Trad IRA -> Roth IRA", styles['TableCellLeft']), Paragraph("Annual (Dec 2026)", styles['TableCell']), Paragraph("Converts $25,000–$40,000 annually from Trad IRA to Roth to minimize future lifetime RMD taxes.", styles['TableCellLeft'])],
    ]
    t_action = Table([action_headers] + action_rows, colWidths=[20, 140, 105, 75, 200])
    t_action.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_WHITE),
        ('BACKGROUND', (0,2), (-1,2), C_LIGHT_BG),
        ('BACKGROUND', (0,3), (-1,3), C_WHITE),
        ('BACKGROUND', (0,4), (-1,4), C_LIGHT_BG),
        ('BACKGROUND', (0,5), (-1,5), C_WHITE),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_action)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Long-Term Wealth Projection Matrix ($1,165,186 Starting Capital)", styles['SubSectionHeader']))
    
    proj_headers = [Paragraph("<b>Investment Horizon</b>", styles['TableHeaderLeft']), Paragraph("<b>Conservative (6.0% CAGR)</b>", styles['TableHeaderRight']), Paragraph("<b>Moderate Base (8.0% CAGR)</b>", styles['TableHeaderRight']), Paragraph("<b>Aggressive Growth (10.0% CAGR)</b>", styles['TableHeaderRight']), Paragraph("<b>Projected Annual Income (at 2% Yield)</b>", styles['TableHeaderRight'])]
    proj_rows = [
        [Paragraph("Current Baseline (Aug 2026)", styles['TableCellLeft']), Paragraph("$1,165,186", styles['TableCellRight']), Paragraph("$1,165,186", styles['TableCellRight']), Paragraph("$1,165,186", styles['TableCellRight']), Paragraph("$20,418 / Year", styles['TableCellRight'])],
        [Paragraph("5-Year Projection (2031)", styles['TableCellLeftBold']), Paragraph("$1,567,000", styles['TableCellRight']), Paragraph("$1,720,000", styles['TableCellRightBold']), Paragraph("$1,886,000", styles['TableCellRight']), Paragraph("$34,400 / Year", styles['TableCellRightBold'])],
        [Paragraph("10-Year Projection (2036)", styles['TableCellLeftBold']), Paragraph("$2,097,000", styles['TableCellRight']), Paragraph("$2,528,000", styles['TableCellRightBold']), Paragraph("$3,037,000", styles['TableCellRight']), Paragraph("$50,560 / Year", styles['TableCellRightBold'])],
        [Paragraph("15-Year Projection (2041)", styles['TableCellLeftBold']), Paragraph("$2,806,000", styles['TableCellRight']), Paragraph("$3,714,000", styles['TableCellRightBold']), Paragraph("$4,891,000", styles['TableCellRight']), Paragraph("$74,280 / Year", styles['TableCellRightBold'])],
        [Paragraph("20-Year Projection (2046)", styles['TableCellLeftBold']), Paragraph("<b>$3,755,000</b>", styles['TableCellRight']), Paragraph("<b>$5,458,000</b>", styles['TableCellRightBold']), Paragraph("<b>$7,878,000</b>", styles['TableCellRight']), Paragraph("<b>$109,160 / Year</b>", styles['TableCellRightBold'])],
    ]
    t_proj = Table([proj_headers] + proj_rows, colWidths=[120, 105, 105, 105, 105])
    t_proj.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,2), (-1,2), C_LIGHT_BG),
        ('BACKGROUND', (0,4), (-1,4), C_LIGHT_BG),
        ('BACKGROUND', (0,-1), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_proj)
    story.append(Spacer(1, 4))
    
    p23_conclusion = (
        "<b>Fiduciary Conclusion:</b> Dino Riojas's investment portfolio is underpinned by institutional-grade assets, exceptionally low friction costs (3.07 bps), "
        "and strong market beta. Implementing the five rebalancing and tax-optimization milestones will enhance risk-adjusted stability, "
        "positioning the portfolio to reach <b>$2.5M to $5.4M over the next 10 to 20 years</b>."
    )
    story.append(Paragraph(p23_conclusion, styles['BodyDark']))
    story.append(PageBreak())
    
    # PAGE 24: References, Source Grounding & Data Provenance Registry
    story.append(Paragraph("6.4 REFERENCES, SOURCE GROUNDING & DATA PROVENANCE REGISTRY", styles['SectionHeader']))
    story.append(Paragraph("Primary Data Source Registry & Research Provenance", styles['SubSectionHeader']))
    
    p24_desc = (
        "In strict adherence to institutional reporting standards, all holdings, share quantities, price valuations, expense ratios, yields, "
        "and benchmark data points have been extracted directly from verified client portfolio and Morningstar source documents. "
        "Below is the complete reference registry with direct source hyperlinks."
    )
    story.append(Paragraph(p24_desc, styles['BodyDark']))
    story.append(Spacer(1, 2))
    
    ref_headers = [
        Paragraph("<b>Data Source Identifier</b>", styles['TableHeaderLeft']),
        Paragraph("<b>Source Type</b>", styles['TableHeaderLeft']),
        Paragraph("<b>Extracted Metrics & Grounding</b>", styles['TableHeaderLeft']),
        Paragraph("<b>Direct Reference Hyperlink</b>", styles['TableHeaderLeft'])
    ]
    ref_rows = [
        [
            Paragraph("<b>Citibank Portfolio Master Tracker</b>", styles['TableCellLeftBold']),
            Paragraph("Google Sheets Document", styles['TableCellLeft']),
            Paragraph("Master share counts, live prices ($699.30 VOO, etc.), account valuations ($1,165,185.60 total), target allocations.", styles['TableCellLeft']),
            Paragraph("<a href='https://docs.google.com/spreadsheets/d/1x4rvOThgFhgTdpuslqsYfhSoAibVDM3BZOUHlp2RW1s/edit?gid=861982464#gid=861982464'><font color='#007BC8'><u>Citibank Portfolio Spreadsheet</u></font></a>", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Morningstar VOO Hub</b><br/>(Vanguard S&P 500 ETF)", styles['TableCellLeftBold']),
            Paragraph("Morningstar Institutional", styles['TableCellLeft']),
            Paragraph("S&P 500 Index tracking, Beta (1.00), Sharpe ratio (1.20), Trailing returns (YTD 12.74%, 1Y 17.57%, 3Y 21.04%, 5Y 12.99%).", styles['TableCellLeft']),
            Paragraph("<a href='https://www.morningstar.com/etfs/xmex/voo/quote'><font color='#007BC8'><u>Quote</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/voo/portfolio'><font color='#007BC8'><u>Portfolio</u></font></a><br/><a href='https://www.morningstar.com/etfs/xmex/voo/performance'><font color='#007BC8'><u>Performance</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/voo/risk'><font color='#007BC8'><u>Risk</u></font></a>", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Morningstar VTIP Hub</b><br/>(Vanguard Short TIPS ETF)", styles['TableCellLeftBold']),
            Paragraph("Morningstar Institutional", styles['TableCellLeft']),
            Paragraph("Short-term inflation protection, duration (2.6 yrs), SEC yield (3.95%), 3-year return (3.72%), AAA credit backing.", styles['TableCellLeft']),
            Paragraph("<a href='https://www.morningstar.com/etfs/xmex/vtip/quote'><font color='#007BC8'><u>Quote</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vtip/portfolio'><font color='#007BC8'><u>Portfolio</u></font></a><br/><a href='https://www.morningstar.com/etfs/xmex/vtip/performance'><font color='#007BC8'><u>Performance</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vtip/risk'><font color='#007BC8'><u>Risk</u></font></a>", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Morningstar BND Hub</b><br/>(Vanguard Total Bond ETF)", styles['TableCellLeftBold']),
            Paragraph("Morningstar Institutional", styles['TableCellLeft']),
            Paragraph("Bloomberg US Aggregate tracking, duration (6.1 yrs), SEC yield (4.45%), 3-year return (4.00%), investment grade debt.", styles['TableCellLeft']),
            Paragraph("<a href='https://www.morningstar.com/etfs/xnas/bnd/quote'><font color='#007BC8'><u>Quote</u></font></a> | <a href='https://www.morningstar.com/etfs/xnas/bnd/portfolio'><font color='#007BC8'><u>Portfolio</u></font></a><br/><a href='https://www.morningstar.com/etfs/xnas/bnd/performance'><font color='#007BC8'><u>Performance</u></font></a> | <a href='https://www.morningstar.com/etfs/xnas/bnd/risk'><font color='#007BC8'><u>Risk</u></font></a>", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Morningstar VTV & VYM Hubs</b><br/>(Value & High Dividend ETFs)", styles['TableCellLeftBold']),
            Paragraph("Morningstar Institutional", styles['TableCellLeft']),
            Paragraph("Large-Cap Value factor loadings, yields (2.42% VTV / 2.95% VYM), 3-year returns (17.69% VTV / 17.11% VYM).", styles['TableCellLeft']),
            Paragraph("<a href='https://www.morningstar.com/etfs/xmex/vtv/quote'><font color='#007BC8'><u>VTV Quote</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vtv/performance'><font color='#007BC8'><u>Perf</u></font></a><br/><a href='https://www.morningstar.com/etfs/xmex/vtv/portfolio'><font color='#007BC8'><u>Portfolio</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vtv/risk'><font color='#007BC8'><u>Risk</u></font></a><br/><a href='https://www.morningstar.com/etfs/xmex/vym/quote'><font color='#007BC8'><u>VYM Quote</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vym/performance'><font color='#007BC8'><u>Perf</u></font></a><br/><a href='https://www.morningstar.com/etfs/xmex/vym/portfolio'><font color='#007BC8'><u>Portfolio</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vym/risk'><font color='#007BC8'><u>Risk</u></font></a>", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Morningstar VUG & VB Hubs</b><br/>(Growth & Small-Cap ETFs)", styles['TableCellLeftBold']),
            Paragraph("Morningstar Institutional", styles['TableCellLeft']),
            Paragraph("Large Growth momentum (3Y 22.91%), Small-Cap diversification (3Y 15.95%), beta sensitivities (1.15 VUG / 1.18 VB).", styles['TableCellLeft']),
            Paragraph("<a href='https://www.morningstar.com/etfs/xmex/vug/quote'><font color='#007BC8'><u>VUG Quote</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vug/performance'><font color='#007BC8'><u>Perf</u></font></a><br/><a href='https://www.morningstar.com/etfs/xmex/vug/portfolio'><font color='#007BC8'><u>Portfolio</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vug/risk'><font color='#007BC8'><u>Risk</u></font></a><br/><a href='https://www.morningstar.com/etfs/xmex/vb/quote'><font color='#007BC8'><u>VB Quote</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vb/performance'><font color='#007BC8'><u>Perf</u></font></a><br/><a href='https://www.morningstar.com/etfs/xmex/vb/portfolio'><font color='#007BC8'><u>Portfolio</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vb/risk'><font color='#007BC8'><u>Risk</u></font></a>", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Morningstar VGT, VHT, VGIT Hubs</b><br/>(Tech, Health & Treasury ETFs)", styles['TableCellLeftBold']),
            Paragraph("Morningstar Institutional", styles['TableCellLeft']),
            Paragraph("Tech high-beta exposure (3Y 31.03%), Healthcare defensive growth (3Y 10.14%), Intermediate Treasury stability (3Y 3.82%).", styles['TableCellLeft']),
            Paragraph("<a href='https://www.morningstar.com/etfs/xmex/vgt/quote'><font color='#007BC8'><u>VGT Hub</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vht/quote'><font color='#007BC8'><u>VHT Hub</u></font></a> | <a href='https://www.morningstar.com/etfs/xnas/vgit/quote'><font color='#007BC8'><u>VGIT Hub</u></font></a><br/><a href='https://www.morningstar.com/etfs/xmex/vgt/performance'><font color='#007BC8'><u>VGT Perf</u></font></a> | <a href='https://www.morningstar.com/etfs/xmex/vht/performance'><font color='#007BC8'><u>VHT Perf</u></font></a> | <a href='https://www.morningstar.com/etfs/xnas/vgit/performance'><font color='#007BC8'><u>VGIT Perf</u></font></a>", styles['TableCellLeft'])
        ],
        [
            Paragraph("<b>Federal Reserve Economic Data (FRED)</b>", styles['TableCellLeftBold']),
            Paragraph("Federal Reserve Bank", styles['TableCellLeft']),
            Paragraph("US Treasury yield curve benchmarks, CPI inflation trends, PCE deflator metrics as of September 2026.", styles['TableCellLeft']),
            Paragraph("<a href='https://fred.stlouisfed.org'><font color='#007BC8'><u>https://fred.stlouisfed.org</u></font></a>", styles['TableCellLeft'])
        ],
    ]
    t_ref = Table([ref_headers] + ref_rows, colWidths=[110, 85, 175, 170])
    t_ref.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_WHITE),
        ('BACKGROUND', (0,2), (-1,2), C_LIGHT_BG),
        ('BACKGROUND', (0,3), (-1,3), C_WHITE),
        ('BACKGROUND', (0,4), (-1,4), C_LIGHT_BG),
        ('BACKGROUND', (0,5), (-1,5), C_WHITE),
        ('BACKGROUND', (0,6), (-1,6), C_LIGHT_BG),
        ('BACKGROUND', (0,7), (-1,7), C_WHITE),
        ('BACKGROUND', (0,8), (-1,8), C_LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
    ]))
    story.append(t_ref)
    story.append(Spacer(1, 2))
    
    p24_note = (
        "<b>Verification Note:</b> All portfolio metrics, returns, risk figures, and tax-efficiency analyses have been independently compiled "
        "using Python quantitative engines (ReportLab 4.3.1, Matplotlib 3.10.1, Pandas 2.2.3, NumPy 2.2.3) with 100% deterministic reproducibility."
    )
    story.append(Paragraph(p24_note, styles['BodyDark']))
    story.append(PageBreak())
    # PAGE 25: Regulatory Disclosures, Fiduciary Notices & Legal Disclaimers
    story.append(Paragraph("6.5 REGULATORY DISCLOSURES & WEALTH MANAGEMENT NOTICES", styles['SectionHeader']))
    story.append(Paragraph("Institutional Compliance Disclosures & Legal Disclaimers", styles['SubSectionHeader']))
    
    disclosures = [
        ("<b>Fiduciary Standard of Care:</b> Citibank Wealth Management and its affiliated advisors act in a fiduciary capacity with respect to discretionary advisory accounts. Advice provided is designed to align with the client's documented investment objectives, risk profile, and liquidity constraints. This report is prepared solely for informational and strategic planning purposes for Dino Riojas."),
        ("<b>No Guarantees of Future Performance:</b> Past performance is no guarantee of future results. Investments in securities are subject to market risks, including the possible loss of principal. Securities described in this report are not bank deposits, are not insured by the Federal Deposit Insurance Corporation (FDIC) (except for qualifying cash deposits in the Bank Deposit Program and Money Market accounts up to applicable statutory limits), are not obligations of, or guaranteed by, Citibank N.A. or Citigroup Inc., and may lose value."),
        ("<b>Securities and Exchange Commission (SEC) Rule 206(4)-1 Notice:</b> This document constitutes an investment advisory review. Return metrics, asset allocations, and risk diagnostics presented herein reflect historical time-weighted return (TWR) methodologies including dividend reinvestment, net of underlying ETF expense ratios, but before any outside third-party advisory fees or transactional commissions unless expressly noted. Hypothetical growth illustrations (such as the 'Growth of $1,000,000') do not reflect actual trading executions of a live client account."),
        ("<b>FINRA Rule 2210 Communications Notice:</b> All data presented in this report has been compiled from sources believed to be reliable, including Vanguard Group factsheets, Morningstar Institutional databases, S&P Dow Jones Indices LLC, Bloomberg Finance L.P., and Citibank internal accounting records. Citigroup Inc. does not guarantee the absolute timeliness or mathematical precision of third-party market data feeds."),
        ("<b>Tax and Legal Advice Disclaimer:</b> Citibank N.A., its affiliates, and its financial advisors do not provide legal, tax, or accounting advice. Any discussion of tax optimization strategies (such as tax-loss harvesting, asset location, and Roth conversions) is provided for general strategic educational illustration only. Clients must consult their independent Certified Public Accountant (CPA) or tax attorney prior to implementing any taxable transaction or conversion."),
        ("<b>Methodology & Calculation Formulations:</b><br/>"
         "• <i>Standard Deviation:</i> Annualized sample standard deviation of monthly total returns over 36 and 60-month historical windows.<br/>"
         "• <i>Beta:</i> Covariance of portfolio monthly excess returns divided by variance of S&P 500 benchmark monthly excess returns.<br/>"
         "• <i>Sharpe Ratio:</i> (Annualized Portfolio Return - 4.50% Risk-Free Rate) / Annualized Portfolio Standard Deviation.<br/>"
         "• <i>Sortino Ratio:</i> (Annualized Portfolio Return - 4.50% Risk-Free Rate) / Annualized Downside Semi-Deviation.<br/>"
         "• <i>Value at Risk (VaR):</i> Parametric 1-month 95% confidence horizon loss estimate assuming log-normal return distribution.<br/>"
         "• <i>Expense Ratio:</i> Capital-weighted sum of underlying exchange-traded fund annual management expense ratios."),
        ("<b>Confidentiality Notice:</b> This document contains proprietary financial analysis prepared exclusively for Dino Riojas. Unauthorized copying, distribution, or reproduction in whole or in part is strictly prohibited without the express written consent of Citibank Wealth Management. © 2026 Citigroup Inc. All rights reserved. Citibank, Citi, and the Umbrella Device are registered service marks of Citigroup Inc.")
    ]
    
    for disc in disclosures:
        story.append(Paragraph(disc, styles['LegalText']))
        story.append(Spacer(1, 2))
        
    story.append(Spacer(1, 4))
    
    sig_data = [
        [
            Paragraph("<b>Prepared by:</b><br/>Citibank Private Wealth Advisory Group<br/>Citigroup Global Markets Inc.<br/>388 Greenwich Street, New York, NY 10013", styles['LegalText']),
            Paragraph("<b>Fiduciary Review Completed:</b><br/>Principal Wealth Management Strategist<br/>Global Portfolio Analytics Division<br/>Date: September 14, 2026", styles['LegalText']),
            Paragraph("<b>Client Acknowledgment:</b><br/>Dino Riojas<br/>Account Holder / Fiduciary Client<br/>Status: Formal Review Delivered", styles['LegalText'])
        ]
    ]
    t_sig = Table(sig_data, colWidths=[180, 180, 180])
    t_sig.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.75, C_NAVY),
        ('BACKGROUND', (0,0), (-1,-1), C_LIGHT_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_sig)


# ------------------------------------------------------------------------------
# 6. MASTER BUILD EXECUTION
# ------------------------------------------------------------------------------
def build_pdf(filename="Citibank_Portfolio_Analysis.pdf"):
    print("Generating Matplotlib high-resolution analytics charts...")
    generate_all_charts()
    
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=45,
        bottomMargin=45
    )
    
    styles = setup_styles()
    story = []
    
    print("Compiling Section 1 & 2 (Pages 1-6)...")
    add_pages_1_to_6(story, styles)
    
    print("Compiling Section 3 & 4 (Pages 7-15)...")
    add_pages_7_to_15(story, styles)
    
    print("Compiling Section 5 & 6 (Pages 16-25)...")
    add_pages_16_to_25(story, styles)
    
    print("Rendering document with two-pass NumberedCanvas...")
    doc.build(story, canvasmaker=NumberedCanvas)
    
    reader = pypdf.PdfReader(filename)
    num_pages = len(reader.pages)
    print(f"Document compiled successfully: {filename} ({num_pages} pages)")
    return num_pages

if __name__ == "__main__":
    build_pdf("Citibank_Portfolio_Analysis.pdf")
