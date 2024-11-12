const marpKrokiPlugin = require('./kroki-plugin')
const marpHideSlidesPlugin = require('./hide-slides-plugin')
const markdownItContainer = require('markdown-it-container')
const markdownItAnchor = require('markdown-it-anchor').default
const markdownItTableOfContents = require('markdown-it-table-of-contents')
//const markdownItTocDoneRight = require('markdown-it-toc-done-right')
const markdownIt = require('markdown-it');
const mdBiblatex = require('./markdown-it-biblatex/src/index.js');

const path = require('path');

module.exports = {
  preprocessor: path.resolve(__dirname, './marp-multi-col.js'),
  engine: ({ marp }) => marp
    .use(marpKrokiPlugin)

    .use(markdownItContainer, 'start-multi-column', {
      render: function(tokens, idx) {
        if (tokens[idx].nesting === 1) {
          return '<div class="columns"><div>\n';
        } else {
          return '</div></div>\n';
        }
      }
    })

    .use(markdownItContainer, 'columns3', {
      render: function(tokens, idx) {
        if (tokens[idx].nesting === 1) {
          return '<div class="columns3"><div>\n';
        } else {
          return '</div></div>\n';
        }
      }
    })
    .use(markdownItContainer, 'columns4', {
      render: function(tokens, idx) {
        if (tokens[idx].nesting === 1) {
          return '<div class="columns4"><div>\n';
        } else {
          return '</div></div>\n';
        }
      }
    })

    .use(markdownItContainer, 'end-column', {
      render: function(tokens, idx) {
        if (tokens[idx].nesting === 1) {
          return '</div><div>\n';
        } else {
          return '</div></div>\n';
        }
      }
    })


    // markdown-it (toc)
    .use(markdownItTableOfContents, {
      "includeLevel": [1, 2]
    })

    // .use(markdownItTocDoneRight, {

    // })

    .use(marpHideSlidesPlugin)

  // markdown-it (biblatex)
  // .use(mdBiblatex, {
  //   bibPath: '../bib/references.bib',
  //   bibliographyTitle: '',
  //   localePath: __dirname + "/csl/locales/locales-en-US.xml",
  //   //stylePath: __dirname + "/csl/styles/apa-numeric-superscript-brackets.csl",
  //   bibliographyEntryWrapper: "p",
  //   wrapBibliography: false,
  //   linkToBibliography: true,
  // })


}


