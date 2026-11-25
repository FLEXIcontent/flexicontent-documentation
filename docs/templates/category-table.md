---
sidebar_position: 9
---

# Table — category view



:::info Source
This page is generated from `site/templates/table/category.xml` and the official FLEXIcontent 5.x language files.
:::

## Template parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout custom title**<br />`custom_layout_title` | This will be displayed to frontend user, e.g. as tooltip of frontend layout switcher | `text` | — | — |

#### Item tabset

### Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Table class**<br />`table_class` | Override Table class. adminlist by default, you can use table table-striped, table table-hover etc in regards of your framework | `text` | — | — |

### Display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Header row (field labels)**<br />`show_field_labels_row` | Show a row with field labels at the top of the items table | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Customize title column header**<br />`customize_titlecol_header` | Choose yes to use a custom header text for title column | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Title column header text**<br />`titlecol_header_text` | Enter column header text. This can be a language string | `text` | — | — |
| **Toggleable columns**<br />`togglable_table_cols` | Allow the user to toggle (hide/show) the table columns | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

### Item title

#### Item title

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
| **Padding top**<br />`title_pad_top` | Internal top spacing _0_ | `number` | — | `0` |
| **Padding left**<br />`title_pad_left` | Internal left spacing _0_ | `number` | — | `0` |
| **Padding right**<br />`title_pad_right` | Internal right spacing _0_ | `number` | — | `0` |
| **Padding bottom**<br />`title_pad_bottom` | Internal bottom spacing _0_ | `number` | — | `0` |

#### Border

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Border radius**<br />`title_border_radius` | Rounding of the borders _0_ | `number` | — | `0` |

### Labels

#### Label styling

#### Colors

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Text color**<br />`label_txt_color` | Choose your text color _#ffffff_ | `fccolor` | — | `#ffffff` |
| **Background color**<br />`label_bg_color` | Choose your background color _#999999_ | `fccolor` | — | `#999999` |

#### Padding

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Padding top**<br />`label_pad_top` | Internal top spacing _2_ | `number` | — | `2` |
| **Padding left**<br />`label_pad_left` | Internal left spacing _4_ | `number` | — | `4` |
| **Padding right**<br />`label_pad_right` | Internal right spacing _4_ | `number` | — | `4` |
| **Padding bottom**<br />`label_pad_bottom` | Internal bottom spacing _2_ | `number` | — | `2` |

#### Border

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Border radius**<br />`label_radius` | Rounding of the borders _3_ | `number` | — | `3` |

### Header row (Field labels)

#### Styling header cells of table

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Text color**<br />`th_txt_color` | Choose your text color | `fccolor` | — | `inherit` |
| **Background color**<br />`th_bg_color` | Choose your background color | `fccolor` | — | `inherit` |

### Item rows (Field values)

#### Styling data cells of table

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Border color**<br />`td_border_color` | Set color of the borders _#dadada_ | `fccolor` | — | `#dadada` |
| **Border width**<br />`td_border_size` | Set thickness of the borders _0_ | `number` | — | `0` |

#### HTML Version

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Text align**<br />`td_txt_align` | Choose text align in cell | `radio` | `inherit` = Inherit<br />`left` = Left<br />`right` = Right<br />`center` = Center | `inherit` (Inherit) |

#### Table styling

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Even rows background**<br />`table_row0_bg_color` | Select the background color of even table rows _#ffffff_ | `fccolor` | — | `#ffffff` |
| **Odd rows background**<br />`table_row1_bg_color` | Select the background color of even table rows _#f7f7f7_ | `fccolor` | — | `#f7f7f7` |
| **Text color**<br />`table_value_color` | Select the color of text inside the table _#555555_ | `fccolor` | — | `#555555` |
| **Hover color**<br />`td_bg_hoverbgcolor` | Set the background color for over td | `fccolor` | — | `inherit` |

#### Item tabset
