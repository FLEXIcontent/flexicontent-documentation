---
sidebar_position: 5
---

# Item template — common options

Item template parameters. They are identical for all four templates (faq, grid, items-tabbed and table).

:::info Source
This page is generated from `site/templates/faq/item.xml` and the official FLEXIcontent 5.x language files.
:::

## Template parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout custom title**<br />`custom_layout_title` | This will be displayed to frontend user, e.g. as tooltip of frontend layout switcher | `text` | — | — |

#### Item tabset

### Item container

:::note
Styling
:::

#### Colors

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Background color**<br />`item_bg_color` | Choose your background color | `fccolor` | — | `inherit` |
| **Text color**<br />`item_text_color` | Choose your text color | `fccolor` | — | `inherit` |

#### Padding

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Padding top**<br />`item_pad_top` | Tmpl item paddingtop desc _0_ | `number` | — | `0` |
| **Padding left**<br />`item_pad_left` | Internal left spacing _0_ | `number` | — | `0` |
| **Padding right**<br />`item_pad_right` | Tmpl item paddingright desc _0_ | `number` | — | `0` |
| **Padding bottom**<br />`item_pad_bottom` | Tmpl padding bottomt desc _0_ | `number` | — | `0` |

#### Border

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Border radius**<br />`item_border_radius` | Rounding of the borders _0_ | `number` | — | `0` |
| **Border color**<br />`item_border_color` | Set color of the borders | `fccolor` | — | `#cccccc` |
| **Border width**<br />`item_border_size` | Set thickness of the borders _0_ | `number` | — | `0` |
| **Border type**<br />`item_border_type` | Select type border solid groove dotted dashed double ridge inset outset _solid_ | `list` | `solid` = solid<br />`dotted` = dotted<br />`dashed` = dashed<br />`double` = double<br />`groove` = groove<br />`ridge` = ridge<br />`inset` = inset<br />`outset` = outset | `solid` (solid) |

### Item title

:::note
Styling
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Title maximum length**<br />`title_cut_text` | Item titles having more characters than this value will be trimmed and appended with ... | `text` | — | — |

#### Colors

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Text color**<br />`title_color` | Choose your text color | `fccolor` | — | `inherit` |
| **Background color**<br />`title_bg_color` | Choose your background color | `fccolor` | — | `inherit` |

#### Padding

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Padding**<br />`title_pad` | Internal top spacing _paddng-top padding-right padding-bottom padding-left in px % rem ect_ | `text` | — | `0` |

#### Border

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Border radius**<br />`title_border_radius` | Rounding of the borders _0_ | `number` | — | `0` |

### Labels

:::note
Styling
:::

#### Colors

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Text color**<br />`label_txt_color` | Choose your text color _#000000_ | `fccolor` | — | `#000000` |
| **Background color**<br />`label_bg_color` | Choose your background color _rgba(255, 255, 255, 0)_ | `fccolor` | — | `rgba(255, 255, 255, 0)` |

#### Padding

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Padding**<br />`label_pad` | Internal top spacing _paddng-top padding-right padding-bottom padding-left in px % rem ect_ | `text` | — | `0` |

#### Border

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Border radius**<br />`label_radius` | Rounding of the borders _0_ | `number` | — | `0` |

### Field positions

:::note
Positions for fields placement
:::

#### Item tabset

### Tabbed

#### Tab Styling

#### Handles

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Background start**<br />`tab_bg_color_start` | Select the starting background color of the TAB, (gradient start) _#3093c7_ | `fccolor` | — | `#3093c7` |
| **Title**<br />`tab_title_color` | Select the color of the TAB text (TAB title) _#3093c7_ | `fccolor` | — | `#3093c7` |

#### Content box

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Text color**<br />`tab_content_bg_color` | Choose your text color _#ffffff_ | `fccolor` | — | `#ffffff` |
| **Border radius**<br />`tab_content_border_radius` | Rounding of the borders _0_ | `number` | — | `0` |
| **Border size top**<br />`tab_content_border_size_top` | Choose size of the separation between tab and content tab _1_ | `number` | — | `1` |
| **Border color top**<br />`tab_content_border_color_top` | Chose the color of the separation between tab and content tab | `fccolor` | — | `#cccccc` |

#### Tab Titles

#### Subtitle Tabset

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Tab 1**<br />`subtitle_tab1_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 2**<br />`subtitle_tab2_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 3**<br />`subtitle_tab3_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 4**<br />`subtitle_tab4_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 5**<br />`subtitle_tab5_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 6**<br />`subtitle_tab6_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 7**<br />`subtitle_tab7_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 8**<br />`subtitle_tab8_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 9**<br />`subtitle_tab9_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 10**<br />`subtitle_tab10_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 11**<br />`subtitle_tab11_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 12**<br />`subtitle_tab12_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |

#### Bottom Tabset

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Tab 1**<br />`bottom_tab1_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 2**<br />`bottom_tab2_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 3**<br />`bottom_tab3_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 4**<br />`bottom_tab4_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 5**<br />`bottom_tab5_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 6**<br />`bottom_tab6_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 7**<br />`bottom_tab7_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 8**<br />`bottom_tab8_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 9**<br />`bottom_tab9_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 10**<br />`bottom_tab10_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 11**<br />`bottom_tab11_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |
| **Tab 12**<br />`bottom_tab12_label` | The text for this label is filtered via JText (you can add to your ini language files) | `text` | — | — |

### Top / Bottom

#### Columns mode

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Top width**<br />`top_col_width` | This is span1 to span12 (100% width). Note 'Top' position is next to 'Image' position the sum of them is 12. If one position is empty the other is expaned to 100% _paddng-top padding-right padding-bottom padding-left in px % rem ect_ | `text` | — | `30%` |
| **Gap**<br />`top_col_gap` | Set gap between image blcok and top block _gap in px % rem etc_ | `text` | — | `2rem` |
| **Top columns**<br />`top_cols` | Number of columns for the top block | `radio` | `—` = Use Global<br />`one` = 1 column<br />`two` = 2 columns | — |
| **Bottom columns**<br />`bottom_cols` | Number of columns for the bottom block | `radio` | `—` = Use Global<br />`one` = 1 column<br />`two` = 2 columns | — |

#### Top box style

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Padding top**<br />`column_pad_top` | Internal top spacing _paddng-top padding-right padding-bottom padding-left in px % rem ect_ | `text` | — | `10px 10px 10px 10px` |
| **Text color**<br />`column_color_top` | Choose your text color | `fccolor` | — | `inherit` |
| **Background color**<br />`column_bg_color_top` | Choose your background color | `fccolor` | — | `transparent` |
| **Border radius**<br />`column_border_radius_top` | Rounding of the borders _0_ | `number` | — | `05` |
| **Border width**<br />`column_border_size_top` | Set thickness of the borders _1_ | `number` | — | `1` |
| **Border color**<br />`column_border_color_top` | Set color of the borders | `fccolor` | — | `#cccccc` |
| **Border type**<br />`column_border_type_top` | Select type border solid groove dotted dashed double ridge inset outset _solid_ | `list` | `solid` = solid<br />`dotted` = dotted<br />`dashed` = dashed<br />`double` = double<br />`groove` = groove<br />`ridge` = ridge<br />`inset` = inset<br />`outset` = outset | `solid` (solid) |

#### Bottom box style

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Padding bottom**<br />`column_pad_bottom` | Internal top spacing _paddng-top padding-right padding-bottom padding-left in px % rem ect_ | `text` | — | `0` |
| **Text color**<br />`column_color_bottom` | Choose your text color | `fccolor` | — | `#cccccc` |
| **Background color**<br />`column_bg_color_bottom` | Choose your background color | `fccolor` | — | `#ffffff` |
| **Border radius**<br />`column_border_radius_bottom` | Rounding of the borders _0_ | `number` | — | `0` |
| **Border width**<br />`column_border_size_bottom` | Set thickness of the borders _1_ | `number` | — | `0` |
| **Border color**<br />`column_border_color_bottom` | Set color of the borders | `fccolor` | — | `#cccccc` |
| **Border type**<br />`column_border_type_bottom` | Select type border solid groove dotted dashed double ridge inset outset _solid_ | `list` | `solid` = solid<br />`dotted` = dotted<br />`dashed` = dashed<br />`double` = double<br />`groove` = groove<br />`ridge` = ridge<br />`inset` = inset<br />`outset` = outset | `solid` (solid) |

### CSS classes

:::note
CSS classes for fields position containers
:::

#### Subtitle

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Subtitle 1**<br />`box_class_subtitle1` | Subtitle1 class desc _flexi group lineinfo subtitle1_ | `text` | — | — |
| **Subtitle 2**<br />`box_class_subtitle2` | Subtitle2 class desc _flexi group lineinfo subtitle2_ | `text` | — | — |
| **Subtitle 3**<br />`box_class_subtitle3` | Subtitle2 class desc _flexi group lineinfo subtitle3_ | `text` | — | — |

#### Subtitle Tabset

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Tab 1**<br />`box_class_subtitle_tab1` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 2**<br />`box_class_subtitle_tab2` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 3**<br />`box_class_subtitle_tab3` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 4**<br />`box_class_subtitle_tab4` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 5**<br />`box_class_subtitle_tab5` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 6**<br />`box_class_subtitle_tab6` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 7**<br />`box_class_subtitle_tab7` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 8**<br />`box_class_subtitle_tab8` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 9**<br />`box_class_subtitle_tab9` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 10**<br />`box_class_subtitle_tab10` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 11**<br />`box_class_subtitle_tab11` | tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 12**<br />`box_class_subtitle_tab12` | Tab class desc _flexi lineinfo_ | `text` | — | — |

#### Main Content

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Image**<br />`box_class_image` | Image class desc _flexi group image_ | `text` | — | — |
| **Top**<br />`box_class_top` | Top class desc _flexi group infoblock_ | `text` | — | — |
| **Description**<br />`box_class_descr` | Description class desc _flexi group description_ | `text` | — | — |

#### Bottom Tabset

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Tab 1**<br />`box_class_bottom_tab1` | Tab1 class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 2**<br />`box_class_bottom_tab2` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 3**<br />`box_class_bottom_tab3` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 4**<br />`box_class_bottom_tab4` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 5**<br />`box_class_bottom_tab5` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 6**<br />`box_class_bottom_tab6` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 7**<br />`box_class_bottom_tab7` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 8**<br />`box_class_bottom_tab8` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 9**<br />`box_class_bottom_tab9` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 10**<br />`box_class_bottom_tab10` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 11**<br />`box_class_bottom_tab11` | Tab class desc _flexi lineinfo_ | `text` | — | — |
| **Tab 12**<br />`box_class_bottom_tab12` | Tab class desc _flexi lineinfo_ | `text` | — | — |

#### Bottom

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Bottom**<br />`box_class_bottom` | Bottomfield class desc _flexi group infoblock_ | `text` | — | — |

#### Item tabset

#### Item tabset
