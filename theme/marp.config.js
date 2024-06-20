const marpKrokiPlugin = require('./kroki-plugin')
const marpHideSlidesPlugin = require('./hide-slides-plugin')
const markdownItContainer = require('markdown-it-container')
const markdownItTableOfContents = require('markdown-it-table-of-contents')
const markdownIt = require('markdown-it');
const mdBiblatex = require('./markdown-it-biblatex/src/index.js');


module.exports = {
  engine: ({ marp }) => marp
  .use(marpKrokiPlugin)

  .use(markdownItContainer, 'columns', {
    render: function (tokens, idx) {
      if (tokens[idx].nesting === 1) {
        return '<div class="columns"><div>\n';
      } else {
        return '</div></div>\n';
      }
    }
  })
  .use(markdownItContainer, 'columns3', {
    render: function (tokens, idx) {
      if (tokens[idx].nesting === 1) {
        return '<div class="columns3"><div>\n';
      } else {
        return '</div></div>\n';
      }
    }
  })
  .use(markdownItContainer, 'columns4', {
    render: function (tokens, idx) {
      if (tokens[idx].nesting === 1) {
        return '<div class="columns4"><div>\n';
      } else {
        return '</div></div>\n';
      }
    }
  })

  .use(markdownItContainer, 'split', {
    render: function (tokens, idx) {
      if (tokens[idx].nesting === 1) {
        return '</div><div>\n';
      } else {
        return '</div></div>\n';
      }
    }
  })

  // markdown-it (toc)
  .use(markdownItTableOfContents, {
    "includeLevel": [1]
  })
  .use(marpHideSlidesPlugin)

  // markdown-it (biblatex)
  .use(mdBiblatex, {
    bibPath: '../bib/reference.bib',
    bibliographyTitle: '',
    localePath: __dirname + "/csl/locales/locales-en-US.xml",
    //stylePath: __dirname + "/csl/styles/apa-numeric-superscript-brackets.csl",
    bibliographyEntryWrapper: "p",
    wrapBibliography: false,
    linkToBibliography: true,
  })


}


