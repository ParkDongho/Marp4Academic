---
target: tasks
marp: true
theme: academic
math: katex
paginate: true
---
<!-- _class: lead -->
<!-- _paginate: false -->
## Marp4Academic

#### Marp Template for Academic Usage

**Dongho Park**

**2022-01-01**


----
<!-- _header: Outline -->

[[toc]]

---
<!-- _class: chapter -->
<!-- _paginate: false -->

# **1. Installation**

---
<!-- _class: chapter -->
<!-- _paginate: false -->

# **3. Diagram**

---
<!-- _header: Wavedrom Example -->

hello world
hello world

:::columns


    ```wavedrom
    { signal: [
      { name: "pclk", wave: 'p.......' },
      { name: "Pclk", wave: 'P.......' },
      { name: "nclk", wave: 'n.......' },
      { name: "Nclk", wave: 'N.......' },
      {},
      { name: 'clk0', wave: 'phnlPHNL' },
      { name: 'clk1', wave: 'xhlhLHl.' },
      { name: 'clk2', wave: 'hpHplnLn' },
      { name: 'clk3', wave: 'nhNhplPl' },
      { name: 'clk4', wave: 'xlh.L.Hx' },
    ]}
    ```


:::split

```wavedrom
{ signal: [
  { name: "pclk", wave: 'p.......' },
  { name: "Pclk", wave: 'P.......' },
  { name: "nclk", wave: 'n.......' },
  { name: "Nclk", wave: 'N.......' },
  {},
  { name: 'clk0', wave: 'phnlPHNL' },
  { name: 'clk1', wave: 'xhlhLHl.' },
  { name: 'clk2', wave: 'hpHplnLn' },
  { name: 'clk3', wave: 'nhNhplPl' },
  { name: 'clk4', wave: 'xlh.L.Hx' },
]}
```

:::

> reference: 
---
<!-- _header: Wavedrom Example -->



---
<!-- _class: chapter -->
<!-- _paginate: false -->

# **4. BibTex Support**

---
<!-- _header: bibtex Example -->

A bibliography [@Cohen-1963] is only produced for the items cited [@Susskind-Hrabovsky-2014].

[@Cohen-1963{see}]

---
<!-- _header: bibtex Type -->

### Regular

A regular citation: [@Cohen-1963]

### Author only

A citation with the author only: [!@Cohen-1963]

### Suppress author

A citation with the author suppressed: [-@Cohen-1963]

### Composite

A composite citation: [~@Cohen-1963]


---
<!-- _header: Anchor Tag -->

A bibliography [@Cohen-1963] is only produced for the items cited [@Susskind-Hrabovsky-2014].

For multiple items in a citation, only the first is linked

Swetlla-2015 [@Swetllla-2015]

[@Swetla-2015]

[@Swetllla-2015]

[@Swetll2la-2015]

[@Cohen-1963]


Eyeriss [@eyeriss]

Eyeriss v2 [@eyeriss-v2]

---
<!-- _class: chapter -->
<!-- _paginate: false -->

# **Appendix**

---
<!-- _header: Bibliography -->

[bibliography]




