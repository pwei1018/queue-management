// Do not remove the eslint-disable camelcase below as the Python data model uses
// snake_case and Vue can't translate it to camelCase easily.
/* eslint-disable camelcase */

export interface User {
  display_name: string
  email: string
  last_name: string
  telephone: string
  user_id: number
  username: string
  send_email_reminders: boolean
  send_sms_reminders: boolean
}

export interface UserUpdateBody {
  email: string
  telephone: string
  send_email_reminders: boolean
  send_sms_reminders: boolean
}
