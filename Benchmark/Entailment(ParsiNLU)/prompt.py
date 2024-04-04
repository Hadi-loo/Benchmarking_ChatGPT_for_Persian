"""PROMPT POOL THAT HAS BEEN USED FOR MATH EVALUATION"""

ENGLISH_ZERO = """\
Natural Language Inference: Read the following premise and hypothesis carefully and determine the relationship between them.
Choose one of the three categories below that best describes their relationship:

- entailment: The meaning of the hypothesis is logically inferred or derived from the premise.
- contradiction: The meaning of the hypothesis contradicts or conflicts with the premise.
- neutral: There is no clear logical relationship between the premise and hypothesis.

Note: The premise and hypothesis are in Persian.

example pattern:
<premise><sep><hypothesis>
<category>:
    entailment or contradiction or neutral

Please select the appropriate category for the given example:
<{premise}><sep><{hypothesis}>
<category>:
    ?\
"""


PERSIAN_ZERO = """\
هدف وظیفه‌ی استنتاج زبان طبیعی تشخیص رابطه‌ی نتیجه‌گیری بین یک <فرضیه> با توجه به یک <پیش‌فرض> است.
رابطه‌ یا برچسب میان آن‌ها می‌تواند یکی از سه نوع تناظر، تناقض یا ناشناخته باشد.
- تناظر : اگر جمله <فرضیه> به طور منطقی نتیجه‌ای از جمله <پیش‌فرض> باشد
- تناقض : اگر جمله <فرضیه> با جمله <پیش‌فرض> در تناقض باشد
- ناشناخته : اگر رابطه‌ای قطعی بین جمله <پیش‌فرض> و جمله <فرضیه> وجود نداشته باشد و هیچ تناظر یا تناقضی نتوان برقرار کرد

الگوی نمونه:
<پیش‌فرض><sep><فرضیه>
<برچسب>:
    تناقض یا تناظر یا ناشناخته

برای نمونه تست زیر نام محتمل‌ترین برچسب را چاپ کن:
<{premise}><sep><{hypothesis}>
<برچسب>:
    ?\
"""


ENGLISH_ONE = """\
Natural Language Inference: Read the following premise and hypothesis carefully and determine the relationship between them.
Choose one of the three categories below that best describes their relationship:

- entailment: The meaning of the hypothesis is logically inferred or derived from the premise.
- contradiction: The meaning of the hypothesis contradicts or conflicts with the premise.
- neutral: There is no clear logical relationship between the premise and hypothesis.

Note: The premise and hypothesis are in Persian.

examples:
<premise><sep><hypothesis>
<category>:
    entailment or contradiction or neutral

<در پس این حمله، کیافخرالدین جلال و سپس کیاوشتاسف به همراه فرزندانشان کشته‌شدند.><sep><آنها ازین مبارزه جان سالم بدر می برند.>
<category>:
    contradiction

<دوستم اینگونه راضیم کرد که من از ارتفاعات فقط وقتی می‌ترسم که به آن فکر می‌کنم ولی وقتی آن بالا می‌رسم برطرف می‌شود.><sep><من از ارتفاعات می‌ترسیدم ولی دوستم مرا قانع کرد.>
<category>:
    entailment

<"یوتی‌ایر اوییشن"، یک شرکت هواپیمایی روسی است که در سال ۱۹۶۷ توسط خطوط هواپیمایی آئروفلوت تأسیس شد و در حال حاضر روزانه به ۷۲ مقصد، در آسیای مرکزی، آسیای جنوبی، آسیای جنوب شرقی، غرب آسیا و اروپا پروازهای مستقیم دارد.><sep><این شرکت یک شرکت دولتی است که بیش از پنجهزار نفر کارمند دارد. >
<category>:
    neutral



Please select the appropriate category for the given example:
<{premise}><sep><{hypothesis}>
<category>:
    ?\
"""


PERSIAN_ONE = """\
هدف وظیفه‌ی استنتاج زبان طبیعی تشخیص رابطه‌ی نتیجه‌گیری بین یک <فرضیه> با توجه به یک <پیش‌فرض> است.
رابطه‌ یا برچسب میان آن‌ها می‌تواند یکی از سه نوع تناظر، تناقض یا ناشناخته باشد.
- تناظر : اگر جمله <فرضیه> به طور منطقی نتیجه‌ای از جمله <پیش‌فرض> باشد
- تناقض : اگر جمله <فرضیه> با جمله <پیش‌فرض> در تناقض باشد
- ناشناخته : اگر رابطه‌ای قطعی بین جمله <پیش‌فرض> و جمله <فرضیه> وجود نداشته باشد و هیچ تناظر یا تناقضی نتوان برقرار کرد

مثال:
<پیش‌فرض><sep><فرضیه>
<برچسب>:
    تناقض یا تناظر یا ناشناخته

<در پس این حمله، کیافخرالدین جلال و سپس کیاوشتاسف به همراه فرزندانشان کشته‌شدند.><sep><آنها ازین مبارزه جان سالم بدر می برند.>
<برچسب>:
    تناقض

<دوستم اینگونه راضیم کرد که من از ارتفاعات فقط وقتی می‌ترسم که به آن فکر می‌کنم ولی وقتی آن بالا می‌رسم برطرف می‌شود.><sep><من از ارتفاعات می‌ترسیدم ولی دوستم مرا قانع کرد.>
<برچسب>:
    تناظر

<"یوتی‌ایر اوییشن"، یک شرکت هواپیمایی روسی است که در سال ۱۹۶۷ توسط خطوط هواپیمایی آئروفلوت تأسیس شد و در حال حاضر روزانه به ۷۲ مقصد، در آسیای مرکزی، آسیای جنوبی، آسیای جنوب شرقی، غرب آسیا و اروپا پروازهای مستقیم دارد.><sep><این شرکت یک شرکت دولتی است که بیش از پنجهزار نفر کارمند دارد. >
<برچسب>:
    ناشناخته



برای نمونه تست زیر نام محتمل‌ترین برچسب را چاپ کن:
<{premise}><sep><{hypothesis}>
<برچسب>:
    ?\
"""


ENGLISH_THREE = """\
Natural Language Inference: Read the following premise and hypothesis carefully and determine the relationship between them.
Choose one of the three categories below that best describes their relationship:

- entailment: The meaning of the hypothesis is logically inferred or derived from the premise.
- contradiction: The meaning of the hypothesis contradicts or conflicts with the premise.
- neutral: There is no clear logical relationship between the premise and hypothesis.

Note: The premise and hypothesis are in Persian.

examples:
<premise><sep><hypothesis>
<category>:
    entailment or contradiction or neutral

<گرچه فیلم موفق بود اما نقش او در این میان نادیده گرفته شد.><sep><در سال ۱۹۴۹ در فیلم اسکاری نامه‌ای به سه همسر ظاهر شد.>
<category>:
    neutral

<من همیشه شنیده ام که شما انقلابیون زندگی را ارزان پنداشته اید ، اما به نظر می رسد وقتی پای زندگی خود شما در میان باشد، قضیه فرق میکند><sep><من دائماً شنیده ام که شما انقلابیون برای زندگی بسیار ارزش قائل هستید.>
<category>:
    contradiction

<در پایان او آهی طولانی سر داد.><sep><او در پایان آهسته آهی کشید.>
<category>:
    entailment

<در پس این حمله، کیافخرالدین جلال و سپس کیاوشتاسف به همراه فرزندانشان کشته‌شدند.><sep><آنها ازین مبارزه جان سالم بدر می برند.>
<category>:
    contradiction

<باغ وحش ادینبورگ هر روز در طول تابستان رژه پنگوئن ها برگزار می کند.><sep><همه بازدید کنندگان تابستانی باغ وحش ادینبورگ، رژه پنگوئن ها را می بینند.>
<category>:
    neutral

<اخیرا برخی از نویسندگان اطلاعات مختصری از این قلعه ارائه داده‌اند که بیشتر منحصر به شکل ظاهری آن است و بنابراین از حیث علمی قابل استناد نیست.><sep><اطلاعات ارائه شده بیشتر مربوط به قدمت ساخت قلعه بود.>
<category>:
    contradiction

<این مزایا نتیجه کنگره یا ادارات و آژانس های فدرال است که توصیه های ما را برای کارآمدتر کردن خدمات دولت ، بهبود بودجه و هزینه های دلار مالیاتی و تقویت مدیریت منابع فدرال انجام می دهند.><sep><ما مسئول پیشرفت در مدیریت منابع فدرال هستیم.>
<category>:
    entailment

<دوستم اینگونه راضیم کرد که من از ارتفاعات فقط وقتی می‌ترسم که به آن فکر می‌کنم ولی وقتی آن بالا می‌رسم برطرف می‌شود.><sep><من از ارتفاعات می‌ترسیدم ولی دوستم مرا قانع کرد.>
<category>:
    entailment

<"یوتی‌ایر اوییشن"، یک شرکت هواپیمایی روسی است که در سال ۱۹۶۷ توسط خطوط هواپیمایی آئروفلوت تأسیس شد و در حال حاضر روزانه به ۷۲ مقصد، در آسیای مرکزی، آسیای جنوبی، آسیای جنوب شرقی، غرب آسیا و اروپا پروازهای مستقیم دارد.><sep><این شرکت یک شرکت دولتی است که بیش از پنجهزار نفر کارمند دارد. >
<category>:
    neutral



Please select the appropriate category for the given example:
<{premise}><sep><{hypothesis}>
<category>:
    ?\
"""


PERSIAN_THREE = """\
هدف وظیفه‌ی استنتاج زبان طبیعی تشخیص رابطه‌ی نتیجه‌گیری بین یک <فرضیه> با توجه به یک <پیش‌فرض> است.
رابطه‌ یا برچسب میان آن‌ها می‌تواند یکی از سه نوع تناظر، تناقض یا ناشناخته باشد.
- تناظر : اگر جمله <فرضیه> به طور منطقی نتیجه‌ای از جمله <پیش‌فرض> باشد
- تناقض : اگر جمله <فرضیه> با جمله <پیش‌فرض> در تناقض باشد
- ناشناخته : اگر رابطه‌ای قطعی بین جمله <پیش‌فرض> و جمله <فرضیه> وجود نداشته باشد و هیچ تناظر یا تناقضی نتوان برقرار کرد

مثال:
<پیش‌فرض><sep><فرضیه>
<برچسب>:
    تناقض یا تناظر یا ناشناخته

<گرچه فیلم موفق بود اما نقش او در این میان نادیده گرفته شد.><sep><در سال ۱۹۴۹ در فیلم اسکاری نامه‌ای به سه همسر ظاهر شد.>
<برچسب>:
    ناشناخته

<من همیشه شنیده ام که شما انقلابیون زندگی را ارزان پنداشته اید ، اما به نظر می رسد وقتی پای زندگی خود شما در میان باشد، قضیه فرق میکند><sep><من دائماً شنیده ام که شما انقلابیون برای زندگی بسیار ارزش قائل هستید.>
<برچسب>:
    تناقض

<در پایان او آهی طولانی سر داد.><sep><او در پایان آهسته آهی کشید.>
<برچسب>:
    تناظر

<در پس این حمله، کیافخرالدین جلال و سپس کیاوشتاسف به همراه فرزندانشان کشته‌شدند.><sep><آنها ازین مبارزه جان سالم بدر می برند.>
<برچسب>:
    تناقض

<باغ وحش ادینبورگ هر روز در طول تابستان رژه پنگوئن ها برگزار می کند.><sep><همه بازدید کنندگان تابستانی باغ وحش ادینبورگ، رژه پنگوئن ها را می بینند.>
<برچسب>:
    ناشناخته

<اخیرا برخی از نویسندگان اطلاعات مختصری از این قلعه ارائه داده‌اند که بیشتر منحصر به شکل ظاهری آن است و بنابراین از حیث علمی قابل استناد نیست.><sep><اطلاعات ارائه شده بیشتر مربوط به قدمت ساخت قلعه بود.>
<برچسب>:
    تناقض

<این مزایا نتیجه کنگره یا ادارات و آژانس های فدرال است که توصیه های ما را برای کارآمدتر کردن خدمات دولت ، بهبود بودجه و هزینه های دلار مالیاتی و تقویت مدیریت منابع فدرال انجام می دهند.><sep><ما مسئول پیشرفت در مدیریت منابع فدرال هستیم.>
<برچسب>:
    تناظر

<دوستم اینگونه راضیم کرد که من از ارتفاعات فقط وقتی می‌ترسم که به آن فکر می‌کنم ولی وقتی آن بالا می‌رسم برطرف می‌شود.><sep><من از ارتفاعات می‌ترسیدم ولی دوستم مرا قانع کرد.>
<برچسب>:
    تناظر

<"یوتی‌ایر اوییشن"، یک شرکت هواپیمایی روسی است که در سال ۱۹۶۷ توسط خطوط هواپیمایی آئروفلوت تأسیس شد و در حال حاضر روزانه به ۷۲ مقصد، در آسیای مرکزی، آسیای جنوبی، آسیای جنوب شرقی، غرب آسیا و اروپا پروازهای مستقیم دارد.><sep><این شرکت یک شرکت دولتی است که بیش از پنجهزار نفر کارمند دارد. >
<برچسب>:
    ناشناخته



برای نمونه تست زیر نام محتمل‌ترین برچسب را چاپ کن:
<{premise}><sep><{hypothesis}>
<برچسب>:
    ?\
"""

